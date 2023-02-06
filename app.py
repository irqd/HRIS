from hris import create_app

app = create_app()
# checks if the app.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True, threaded=True)