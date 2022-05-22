from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__, template_folder='./app/templates/')

manager = Manager(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__=='__main__':
    manager.run()
