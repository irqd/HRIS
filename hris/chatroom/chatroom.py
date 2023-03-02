from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_socketio import join_room, leave_room, send, SocketIO

from hris import socketio
from hris.models import *


chatroom_bp: Blueprint = Blueprint('chatroom_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='chatroom_bp.static')


@chatroom_bp.route('/chatroom', methods=['GET', 'POST'])
def chat():

    #  if request.method == "POST":
    #     name = request.form.get("name")
    #     code = request.form.get("code")
    #     join = request.form.get("join", False)
    #     create = request.form.get("create", False)

    #     if not name:
    #         return render_template("home.html", error="Please enter a name.", code=code, name=name)

    #     if join != False and not code:
    #         return render_template("home.html", error="Please enter a room code.", code=code, name=name)
        
    #     room = code
    #     if create != False:
    #         room = generate_unique_code(4)
    #         rooms[room] = {"members": 0, "messages": []}
    #     elif code not in rooms:
    #         return render_template("home.html", error="Room does not exist.", code=code, name=name)
        
    #     session["room"] = room
    #     session["name"] = name
    #     return redirect(url_for("room"))

    # balak ko sana mag block content para nagpapalit palit yung nasa right (yung mga message) kung anong romm ang napindot sa left
    # sa tutorial kasi page gamit nya kaya nag form post tapos punta sa ibang route

    # room = session.get("room")
    # if room is None or session.get("name") is None or room not in rooms:
    # put it in jinja -> chat.html


    return render_template('chat.html')

rooms = {}


@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return 
    
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    
    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")
