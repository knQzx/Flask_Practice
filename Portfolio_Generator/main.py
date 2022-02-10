from flask import Flask, render_template


app = Flask(__name__, static_folder='', template_folder='')


@app.route('/')
def index():
    object_Data = {
        'name_user': 'Novikov Kira',
        'briefly_about_yourself': 'I am a programmer, currently studying Flask, Node.js and Django. ',
        'telegram_url': 'https://t.me/knQzx',
        'github_url': 'https://github.com/knQzx',
        'about_me': "I am a novice programmer, I am fifteen years old. I graduated from Yandex.Lyceum 1st year, and now I'm finishing the second year. At the moment I'm also studying Flask, Node JS and Django, and I'm trying to write mini projects on these topics. You can write to me at the email address listed below.",
        'email_user': 'nov-kir.n@yandex.ru',
        'first_course': 'Yandex Lyceum',
        'second_course': 'NodeJS The Net Ninja Course',
        'who_did_you_study_for_1': 'Python Developer',
        'who_did_you_study_for_2': 'NodeJS Course',
        'first_date_course': 'November 1, 2020 - May 2022',
        'second_date_course': 'January 1 2022 - PRESENT',
        'first_course_data': 'I really enjoyed taking the Python course at Yandex Lyceum, because it gave me the basics of understanding what to study next and what to strive for. There I mastered the basics of Python, as well as Qt, PyGame, and am currently studying Flask.',
        'second_course_data': 'In this course I am learning the basics of Node JS and writing my mini projects.'
    }
    skills = [['90', 'Python'], ['80', 'Javascript'], ['75', 'NodeJS'], ['75', 'FLASK'],
              ['65', 'HTML'], ['60', 'Django']]
    return render_template('index.html', **object_Data, skills=skills)


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
