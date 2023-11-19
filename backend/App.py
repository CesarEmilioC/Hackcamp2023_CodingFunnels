from flask import Flask, render_template, request, redirect, url_for
import json

with open('Users.json') as file:
    user_data = json.load(file)

app = Flask(__name__, template_folder='frontend')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']

        # Check if the username already exists
        if username in user_data:
            # Redirect to another page if the username exists
            return redirect(url_for('dashboard', username=username))
        else:
            # Show an error message if the username doesn't exist
            error_message = "Username does not exist. Please register."
            return render_template('index.html', error_message=error_message)

    return render_template('register.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    return f"Welcome, {username}!"

if __name__ == '__main__':
    app.run(debug=True)