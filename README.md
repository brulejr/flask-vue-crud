# Developing a Single Page App with Flask and Vue.js

## Features
### Backend
* [Minimal Flask 1.0 App](https://www.fullstackpython.com/flask.html) Python Microservice Framework
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) API with class-based secure resource routing
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) API for ORM database access
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) API that handle SQLAlchemy changes
### Frontend
* [vue-cli 3](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md)
* [Vuex](https://vuex.vuejs.org/)
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://github.com/axios/axios/) for backend communication
  * [axios-auth-refresh](https://github.com/Flyrell/axios-auth-refresh) for automatic token refresh

## Want to use this project?

1. Fork/Clone

1. Run the server-side Flask app in one terminal window:

    ```sh
    $ cd server
    $ python3 -m venv env
    $ source env/bin/activate
    (env)$ pip3 install -r requirements.txt
    (env)$ flask db upgrade
    (env)$ flask run
    ```

    Navigate to [http://localhost:5000](http://localhost:5000)

1. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client-vuetify
    $ npm install
    $ npm run serve
    ```

    Navigate to [http://localhost:8080](http://localhost:8080)

## Want to learn how to build this?

Check out the [post](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs).

## Resources
* Other project
  * https://github.com/gtalarico/flask-vuejs-template
  * https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
  * https://github.com/PythonToDoList/flask/blob/master/flask_todo/app.py
