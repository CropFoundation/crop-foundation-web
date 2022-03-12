from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    # put application's code here
    organization = 'Crop Foundation'
    return render_template('index.html')


@app.route('/planter')
def planter():
    return render_template('planter.html')


if __name__ == '__main__':
    app.run()
