from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def planet_sample(planet_name):
    planet_name = planet_name.lower().title()
    if planet_name == 'Марс':
        fi_message = 'Марс меньше Земли и Венеры'
        se_message = 'Он обладает атмосферой'
        th_message = 'С поверхностным давлением 6,1 мбар'
        fo_message = 'На его поверхности есть вулканы'
        fi_message = 'Красный цвет вызван количеством оксида железа'
    elif planet_name == 'Земля':
        fi_message = 'У Земли наблюдается тектоника плит'
        se_message = 'Земля является уникальной'
        th_message = 'Атмосфера Земли содержит свободный кислород'
        fo_message = 'У Земли есть один естественный спутник'
        fi_message = 'На земле есть жизнь'
    elif planet_name == 'Венера':
        fi_message = 'Венера близка по размеру к Землет'
        se_message = 'Имеет толстую силикатную оболочку вокруг железного ядра'
        th_message = 'Имеет атмосферу вокруг железного ядра'
        fo_message = 'Её атмосфера в 90 раз плотнее Земли'
        fi_message = 'У Венеры нет спутников'
    elif planet_name == 'Меркурий':
        fi_message = 'Является ближайшей планетой к Солнцу'
        se_message = 'Наименьшая планетная система'
        th_message = 'У планеты нет спутников'
        fo_message = 'Меркурий имеет крайне разреженную атмосферу'
        fi_message = 'Присутствуют лопастевидные уступы'
    elif planet_name == 'Юпитер':
        fi_message = 'Юпитер обладает массой в 318 раз больше земной'
        se_message = 'И в 2,5 раза массивнее всех остальных планет'
        th_message = 'Он состоит главным образом из водорода и гелия'
        fo_message = 'Высокая внутренняя температура'
        fi_message = 'У Юпитера имеется 79 спутников'
    elif planet_name == 'Сатурн':
        fi_message = 'Известный своей обширной системой колец'
        se_message = 'Имеет схожие с Юпитером структуру атмосферы и магнитосферы'
        th_message = 'Объём Сатурна составляет 60 % юпитерианского'
        fo_message = '95 масс Земли'
        fi_message = 'Сатурн — наименее плотная планета Солнечной системы'
    elif planet_name == 'Уран':
        fi_message = 'Уран имеет массу в 14 раз больше, чем Земля'
        se_message = 'Являясь самым лёгким среди планет-гигантов'
        th_message = 'Он вращается «лёжа на боку»'
        fo_message = 'Плоскость экватора Урана наклонена к плоскости его орбиты'
        fi_message = 'У Урана открыты 27 спутников'
    elif planet_name == 'Нептун':
        fi_message = 'Нептун немного меньше Урана'
        se_message = '17 масс Земли'
        th_message = 'Он излучает много внутреннего тепла'
        fo_message = 'У Нептуна имеется 14 известных спутников'
        fi_message = 'Крупнейший — Тритон'
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
      <title>Варианты выбора</title>
    </head>
    <body>
        <h1>Мое предложение: {planet_name}</h1><br>
        <h4>{fi_message}</h4>
        <div class="alert alert-success" role="alert">
            {se_message}
        </div>
        <div class="alert alert-secondary" role="alert">
            {th_message}
        </div>
        <div class="alert alert-warning" role="alert">
            {fo_message}
        </div>
        <div class="alert alert-danger" role="alert">
            {fi_message}
        </div>
    </body>
    </html>
    """
    return html


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
