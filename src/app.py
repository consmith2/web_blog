from src.common.database import Database
from src.models.blog import Blog
from src.models.post import Post
from src.models.user import User


__author__ = 'cjs'


from flask import Flask, render_template, request

app = Flask(__name__) #  '__main__'
app.secret_key = "conrad"

@app.route('/') # www.mysite.com/api/
def hello_method():
    return render_template('login.html')

@app.before_first_request
def initialize_database():
    Database.initialize

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)

    return render_template;("profile.html", email.session['email'])

if __name__ ==  '__main__':
    app.run(port=4995)
