from flask import Flask, render_template

app = Flask(__name__)

# Определяем маршрут для обработки GET-запросов
@app.route('/', methods=['GET'])
def get_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()