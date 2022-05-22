from flask import Flask, render_template
from flask_script import Manager

#static_folder参数和template_folde参数需要设置
app = Flask(__name__, static_folder = './app/static/', template_folder='./app/templates/')

manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__=='__main__':
    manager.run()
