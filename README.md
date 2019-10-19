# Developing a Single Page App with Flask and Vue.js

### Want to learn how to build this?

Check out the [post](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs).

## Want to use this project?

1. Fork/Clone

1. Run the server-side Flask app in one terminal window:

    ```sh
    $ cd server
    $ python3.7 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ flask db upgrade
    (env)$ flask run
    ```

    Navigate to [http://localhost:5000](http://localhost:5000)

1. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client
    $ npm install
    $ npm run serve
    ```

    Navigate to [http://localhost:8080](http://localhost:8080)

## Resources
* [Flask-RESTPlus]([https://flask-restplus.readthedocs.io/en/stable/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* Other project
  * https://github.com/gtalarico/flask-vuejs-template
  * https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
