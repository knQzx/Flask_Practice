from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="2name" aria-describedby="emailHelp" placeholder="Введите фамилию" name="2name">
                                    <input type="text" class="form-control" id="1name" aria-describedby="emailHelp" placeholder="Введите имя" name="1name"><br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Неполное среднее</option>
                                          <option>Среднее</option>
                                          <option>Неполное высшее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div><br>
                                    <label for="classSelect">Какие у Вас есть профессии?</label><br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules1" name="accept1">
                                        <label class="form-check-label" for="acceptRules1">инженер-исследователь</label><br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules2" name="accept2">
                                        <label class="form-check-label" for="acceptRules2x">пилот</label><br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules3" name="accept3">
                                        <label class="form-check-label" for="acceptRules3">строитель</label><br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules4" name="accept4">
                                        <label class="form-check-label" for="acceptRules4">экзобиолог</label><br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules5" name="accept5">
                                        <label class="form-check-label" for="acceptRules5">врач</label><br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules6" name="accept6">
                                        <label class="form-check-label" for="acceptRules6">инженер по терраформированию</label><br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules7" name="accept7">
                                        <label class="form-check-label" for="acceptRules7">климатолог</label><br>
                                        <input type="checkbox" class="form-check-input" id="acceptRules8" name="accept8">
                                        <label class="form-check-label" for="acceptRules8">специалист по радиационной защите</label><br>
                                    </div><br>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div><br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div><br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div><br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div><br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
