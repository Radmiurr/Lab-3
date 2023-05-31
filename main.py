from flask import Flask, render_template, request
import math


# Инициализация приложения
app = Flask(__name__)


# Корневой маршрут для вывода формы
@app.route('/')
def index():
    return render_template('index.html')


# Маршрут для обработки формы
@app.route('/calculate_volume', methods=['POST'])
def calculate_volume():
    # Получаем данные из формы
    shape = request.form.get('shape')

    # Вычисляем объем геометрической фигуры
    if shape == 'cube':
        side = float(request.form.get('side'))
        precision = int(request.form.get('precision'))
        volume = round(side ** 3, precision)
    elif shape == 'sphere':
        precision = int(request.form.get('precision'))
        radius = float(request.form.get('radius'))
        volume = round(4 / 3 * math.pi * radius ** 3, precision)
    elif shape == 'cylinder':
        precision = int(request.form.get('precision'))
        radius = float(request.form.get('radius'))
        height = float(request.form.get('height'))
        volume = round(math.pi * radius ** 2 * height, precision)

    # Выводим результат в шаблон HTML
    return render_template('index.html', shape=shape, volume=volume)


if __name__ == '__main__':
    app.run(debug=True)