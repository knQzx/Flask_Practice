from flask import Flask

app = Flask(__name__)


@app.route('/promotion')
def index():
    result = []
    for el in ['Человечество вырастает из детства.',
                'Человечеству мала одна планета.',
                'Мы сделаем обитаемыми безжизненные пока планеты.',
                'И начнем с Марса!',
                'Присоединяйся!']:
        result.append(f'<p>{el}</p>')
    return "\n".join(result)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
