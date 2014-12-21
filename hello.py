from flask import Flask, render_template, request, redirect, url_for, session, flash
import controllers
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', username = "")

@app.route('/', methods =['POST'])
def login():
	username = request.form['username']


@app.route('/<username>')
def userPage(username):
	user = username
	return render_template('index.html', username = user)


@app.route('/logout')
def logout():
	return redirect('/')

# test code 
@app.route('/user/<username>')
def hello(username):
	return 'hey %s!' % username

if __name__ == '__main__':
    app.run(debug=True)

