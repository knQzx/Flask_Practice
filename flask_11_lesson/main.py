from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/list_prof/<list_type>')
def index(list_type):
    list_val = ['ds', 'dsfdssd', 'fds']
    if list_type == 'ol':
        return render_template('index.html', title='Домашняя страница', list_type=list_type, list_values=list_val)
    elif list_type == 'ul':
        return render_template('index.html', title='Домашняя страница', list_type=list_type, list_values=list_val)
    else:
        return "Error parameter! ('ol' or 'ul')"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
