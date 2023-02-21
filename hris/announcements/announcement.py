from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import desc
from .forms import *

announcement_bp = Blueprint('announcement_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='announcement/static')

@announcement_bp.route('/announcements', methods=['GET', 'POST'])
@login_required
def announcements():
    add_announcement = AnnouncementModal()
    announcements = Announcements.query.filter_by(user_id = current_user.id).order_by(Announcements.id.desc()).all()

    return render_template('announcements.html', add_announcement=add_announcement, announcements=announcements)

@announcement_bp.route('/announcements/add_announcement', methods=['POST'])
@login_required
def add_announcement(): 
    add_announcement = AnnouncementModal(request.form)
   

    if request.method == 'POST':
        if add_announcement.validate_on_submit():
            announcement = Announcements(
                title = add_announcement.title.data,
                announced_by = add_announcement.announced_by.data,
                message = add_announcement.message.data,
                user_id = current_user.id
            )

            db.session.add(announcement)
            db.session.commit()
        
            flash(f'{current_user.name} added new announcement!', category='success')

    return redirect(url_for('announcement_bp.announcements'))

@announcement_bp.route('/announcements/delete_announcement', methods=['POST'])
@login_required
def delete_announcement(): 
    if request.method == 'POST':
        
        announcement_id = request.form.get('announcement_id')
        Announcements.query.filter_by(id = announcement_id).delete()
        db.session.commit()

        flash('Announcement Deleted!', category='danger')

    return redirect(url_for('announcement_bp.announcements'))

@announcement_bp.route('/announcements/edit_announcement', methods=['POST'])
@login_required
def edit_announcement(): 
    if request.method == 'POST':
        edit_modal = AnnouncementModal(request.form)
        announcement_id = request.form.get('announcement_id')

        if edit_modal.validate_on_submit:
            edited_announcement = Announcements.query.filter_by(id = announcement_id).first()
            
            edited_announcement.title = edit_modal.title.data
            edited_announcement.message = edit_modal.message.data

            db.session.commit()

            flash('Announcement Edited!', category='warning')

    return redirect(url_for('announcement_bp.announcements'))