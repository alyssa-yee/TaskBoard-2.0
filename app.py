from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from db import add_user, find_user, task_select_by_group_name, get_groups, group_select_from_username, find_group, add_user_to_group, insert_task
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# View routes
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/taskboard')
def taskboard():
    curr_user = session.get('username')
    group = group_select_from_username(curr_user)
    tasks = task_select_by_group_name(group[0])
    return render_template('Taskboard.html', tasks = tasks, group = group[0])

@app.route('/motivation')
def motivation():
    return render_template('Motivation.html')

@app.route('/group')
def group():
    groups = get_groups()
    return render_template('group.html', groups = groups)

# Request Routes
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/login_submit', methods=['POST'])
def login_submit():
    username_var = request.form['login_username']
    fetched = find_user(username_var)
    if fetched is not None:
        if check_password_hash(fetched[2], request.form['login_password']):
            print("Successfully logged in!")
            session['username'] = fetched[1]
            return redirect(url_for('group'))
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
        session['username'] = username_var
        print("Registration successful! User: " + username_var + " created!")
        return redirect(url_for('group'))
    except:
        print("Registration failed, username invalid or already taken")
        return redirect(url_for('register'))
    
@app.route('/join_group', methods =['POST'])
def join_group():
    curr_user = session.get('username')
    user = find_user(curr_user)
    selected_group = find_group(request.form['group'])
    add_user_to_group(user[0], selected_group[0])
    session['group'] = selected_group[1]
    return redirect(url_for('taskboard'))

@app.route('/create_task', methods=['POST'])
def create_task():
    group = session.get('group')
    task = request.form['task_name']
    status = request.form['task_status']
    insert_task(task, group, status)
    return redirect(url_for('taskboard'))




# -------------APP RUNNING--------------------
if __name__ == "__main__":
    app.run(debug=True)
