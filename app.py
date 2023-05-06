from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
@app.route('/')
def login():
    return render_template('TaskBoard.html')


@app.route('/login_submit', methods=['POST'])
def login_submit():
    username_var = request.form['login_username']
    password_var = request.form['login_password']
    session['username'] = username_var
    session['password'] = password_var
    return redirect(url_for('login_username_and_password_check'))

# -------------APP RUNNING--------------------
if __name__ == "__main__":
    app.run(debug=True)
