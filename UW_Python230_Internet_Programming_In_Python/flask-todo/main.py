from datetime import datetime
import os
import peewee

from flask import Flask, render_template, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256

from model import Task, User

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()


@app.route('/all')
def all_tasks():
    return render_template('all.jinja2', tasks=Task.select())


@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'username' not in session:
        return redirect(url_for('login'))
    # If the method is POST:
    #    then use the name that the user submitted to create a
    #    new task and save it
    #    Also, redirect the user to the list of all tasks
    # Otherwise, just render the create.jinja2 template
    if request.method == 'POST':
        task_name = request.form['name']
        Task(name=task_name).save()
        return redirect(url_for('all_tasks'))
    else:
        return render_template('create.jinja2')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the user is attempting to submit the login form (method is POST)
    #    Find a user from the database that matches the username provided in the form submission
    #    If you find such a user and their password matches the provided password:
    #        Then log the user in by settings session['username'] to the users name
    #        And redirect the user to the list of all tasks
    #    Else:
    #        Render the login.jinja2 template and include an error message 
    # Else the user is just trying to view the login form
    #    so render the login.jinja2 template
    if request.method == 'POST':
        user_name = request.form['name']
        password_submitted = request.form['password']
        try:
            user = User.get(User.name == user_name)
            if not pbkdf2_sha256.verify(password_submitted, user.password):
                return render_template('login.jinja2', error="Incorrect password.")
        except peewee.DoesNotExist:
            return render_template('login.jinja2', error="Incorrect username.")
        else:
            session['username'] = user_name
            return redirect(url_for('all_tasks'))
    else:
        return render_template('login.jinja2')


@app.route('/incomplete', methods=['GET', 'POST'])
def incomplete_tasks():
    # If the visitor is not logged in as a user:
        # Then redirect them to the login page
    if 'username' not in session:
        return redirect(url_for('login'))

    # If the request method is POST
        # Then retrieve the username from the session and find the associated user
        # Retrieve the task_id from the form submission and use it to find the associated task
        # Update the task to indicate that it has been completed at datetime.now() by the current user 
    # Retrieve a list of all incomplete tasks 
    # Render the incomplete.jinja2 template, injecting in the list of all incomplete tasks
    if request.method == 'POST':
        user_name = session['username']
        try:
            user = User.get(User.name == user_name)
        except peewee.DoesNotExist:
            return render_template('login.jinja2', error="Error: Username does not exist.")
        
        task_id = request.form['task_id']
        try:
            task = Task.get(Task.id == task_id)
        except peewee.DoesNotExist:
            return render_template('incomplete.jinja2', error="Error: Task not found.") 

        task.performed = datetime.now()
        task.performed_by = user
        task.save()

    incomplete_tasks = Task.select().where(Task.performed.is_null())
    return render_template('incomplete.jinja2', tasks=incomplete_tasks)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)