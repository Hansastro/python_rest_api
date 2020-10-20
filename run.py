import Rest_app

if __name__ == '__main__':
    app = Rest_app.create_app()
    app.run(debug=True)