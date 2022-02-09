from flask import Flask

app = Flask(__name__)


@app.route('/promotion_image')
def index():
    return """
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
      <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="https://clipart-best.com/img/mars-planet/mars-planet-clip-art-10.png" width="250" height="250" alt="нема">
        <div class="alert alert-dark" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-success" role="alert">
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-secondary" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div class="alert alert-warning" role="alert">
            И начнем с Марса!
        </div>
        <div class="alert alert-danger" role="alert">
            Присоеденяйся!
        </div>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
