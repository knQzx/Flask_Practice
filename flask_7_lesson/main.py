from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def form_sample(nickname, level, rating):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
      <title>Результаты</title>
    </head>
    <body>
        <h1>Результаты отбора</h1>
        <h4>Претендента на участие в мисии {nickname}</h4>
        <div class="alert alert-success" role="alert">
            Поздравляем! Ваш рейтинг после {level} этапа отбора
        </div>
        <p>составляет {rating}!</p>
        <div class="alert alert-warning" role="alert">
            Желаем удачи!
        </div>
    </body>
    </html>
    """
    return html


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    
