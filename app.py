from flask import Flask
from flask import render_template
from flask import send_file

app = Flask(__name__)


@app.route('/')
def index():
    # put application's code here
    organization = 'Crop Foundation'
    return render_template('index.html')


@app.route('/planter')
def planter():
    return render_template('planter.html')


@app.route('/download')
def download_file():
    path = "download/planter.apk"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run()
