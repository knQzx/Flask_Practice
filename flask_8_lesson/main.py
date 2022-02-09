from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        with open(f'static/photos/{request.files["image"].filename}', 'wb') as file:
            file.write(request.files['image'].read())
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Отбор астронавтов</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link href="static/css/style.css" rel="stylesheet">
</head>
<body>
<h1>Загрузка фотографии</h1>
<h3>Для участия в миссии</h3>
<form class="login_form" method="post" enctype="multipart/form-data">
    <div class="form-group">
        <label class="form-check-label" for="image">Приложите фотографиюююююю</label>
        <input type="file" class="form-control" id="image" name="image">
    </div>
    {'<img max alt=Картинка чисто src=' + url_for('static', filename=f'photos/{request.files["image"].filename}') + '>' if request.method == 'POST' else ""}</br>
    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
