from project import api

application = api.create_app()

if __name__ == "__main__":
    application.run(debug=True)
