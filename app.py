import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return render_template("main.html")


@app.route('/weather')
def weather():
    temperature = random.randint(-30,+30)
    return render_template('weather.html', temperature=temperature)


@app.route('/me')
def not_me():
    return render_template('Pin.html')



# запуск сайта
if __name__ == '__main__':
    app.run(debug=True)
