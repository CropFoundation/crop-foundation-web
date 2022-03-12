from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # put application's code here
    organization = 'Crop Foundation'
    return f'<h1>{organization}</h1>'


if __name__ == '__main__':
    app.run()
