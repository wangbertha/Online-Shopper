from flask import Flask, render_template
import controllers
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yaleims')
def yaleims():
	wks = controllers.overall()
	return render_template('yaleims/home.html', wks=wks)

@app.route('/habitar')
def habitar():
	wks = controllers.overall()
	return render_template('habitar/index.html', wks=wks)

@app.route('/user/<username>')
def hello(username):
	return 'hey %s!' % username

if __name__ == '__main__':
    app.run(debug=True)
