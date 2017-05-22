from flask import Flask

app = Flask(__name__)


@app.route('/f')
@app.route('/f/<celsiusvalue>')
def get_fahrenheit(celsiusvalue=0):
    celsius = float(celsiusvalue)
    fahrenheit = celsius * 9.0 / 5 + 32
    return "{:.2f} C = {:.2f} F".format(celsius, fahrenheit)

@app.route('/c')
@app.route('/c/<fahrenheitvalue>')
def get_celsius(fahrenheitvalue=0):
    fahrenheit = float(fahrenheitvalue)
    celsius = 5 / 9 * (fahrenheit - 32)
    return "{:.2f} F = {:.2f} C".format(fahrenheit, celsius)

if __name__ == '__main__':
    app.run()
