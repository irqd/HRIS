from hris import create_app
from flask import render_template

app = create_app()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# checks if the app.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True, threaded=True)