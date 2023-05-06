from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from db import add_user, find_user
app = Flask(__name__)


# View routes
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/taskboard')
def taskboard():
    return render_template('Taskboard.html')


# Request Routes
@app.route('/login_submit', methods=['POST'])
def login_submit():
    username_var = request.form['login_username']
    fetched = find_user(username_var)
    if fetched is not None:
        if check_password_hash(fetched[2], request.form['login_password']):
            print("Successfully logged in!")
            return redirect(url_for('taskboard'))
        else:
            print("Login failed. Password incorrect")
            return redirect(url_for('login'))
    else:
        print("Login failed. Username not found")
        return redirect(url_for('login'))

@app.route('/register_submit', methods=['POST'])
def register_submit():
    username_var = request.form['register_username']
    hash_pw = generate_password_hash(request.form['register_password'], method = 'sha256')
    print(username_var, hash_pw)
    try:
        add_user(username_var, hash_pw)
        print("Registration successful! User: " + username_var + " created!")
        return redirect(url_for('taskboard'))
    except:
        print("Registration failed, username invalid or already taken")
        return redirect(url_for('register'))
    

# -------------APP RUNNING--------------------
if __name__ == "__main__":
    app.run(debug=True)
