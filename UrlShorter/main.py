import sys
import pyshorteners
from flask import Flask, request, url_for, render_template


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', url='')
    elif request.method == 'POST':
        link_url = request.form['url']
        if 'tinyurl' not in link_url:
            s = pyshorteners.Shortener()
            SHORT_URL = s.tinyurl.short(link_url)
            print(SHORT_URL)
            return render_template('index.html', url=SHORT_URL)
        else:
            return render_template('index.html', url='')


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
