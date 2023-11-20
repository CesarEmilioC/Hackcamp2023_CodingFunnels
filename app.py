from flask import Flask, render_template, request, redirect, url_for
import json

#Import data from json file
with open('json_files/Users.json') as file:
    user_data = json.load(file)

#Initialize program with flask
app = Flask(__name__)

#First route to the login page
@app.route('/', methods=['GET', 'POST'])
def index():
    
    error_message = ""

    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        if username in user_data:
            if user_data[username]["Password"] == password:
                # Redirect to the logged in page if the username exists
                return redirect(url_for('loggedin', username=username))
            else:
                #Error message if the password is incorrect
                error_message = "Password is incorrect. Please check your credentials."
        else:
            #Error message if the username doesn't exist
            error_message = "Username does not exist. Please register."
    
    #Render de login page
    return render_template('index.html', error_message = error_message)

#Route for the logged in page
@app.route('/loggedin/<username>')
def loggedin(username):
    return render_template('user-loggedin.html', username = username)

#Route for the registering page
@app.route('/register_page')
def register_page():
    return render_template('register-account.html')

#Route for registering function
@app.route('/register', methods=['GET', 'POST'])
def register():
    
    register_message = ""

    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        if username in user_data:
            register_message = "Username already exists. Try another one."
        else:
            #Check that the username and password are not blank
            if username != "" and password != "":
                user_data[username] = {"Password": password, "Lost_Items": [], "Found_Items": [], "Status": []}
                #Update json file and go back to login
                with open('json_files/Users.json', 'w') as file:
                    json.dump(user_data, file, indent = 2)
                error_message = f"{username} registered succesfully. You can log in now!"
                return render_template('index.html', error_message = error_message)
            else:
                register_message = "Username and password fields should be filled up."
    #Render the registering page
    return render_template('register-account.html', register_message = register_message)

#Go to report_lost page
@app.route('/report_lost')
def report_lost():
    return render_template('report-lost.html')

#Go to report_found page
@app.route('/report_found')
def report_found():
    return render_template('report-found.html')

#Return to login page
@app.route('/index_return')
def index_return():
    return render_template('index.html')

#Return to user page
@app.route('/user_return')
def user_return():
    return render_template('user-loggedin.html')

if __name__ == '__main__':
    app.run(debug=True)