from flask import Flask

app = Flask(__name__)


@app.route('/image_mars')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Привет, Марс!</title>
    </head>
    <body>
      <h1>Жди нас, Марс!</h1>
      <img src="https://clipart-best.com/img/mars-planet/mars-planet-clip-art-10.png" width="250" height="250" alt="нема">
      <p>Вот она какая, красная планета.</p>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
