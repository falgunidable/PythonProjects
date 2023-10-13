#waitress - helps to serve the app during production
from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)   # this makes it the flask app

# routes that are accessed on the web
@app.route('/')
@app.route('/index')
def index():        # function to return something for the routes
    # return 'Hello World !'
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # check for empty strings or strings with spaces
    if not bool(city.strip()):
        city = 'Pune'

    weather_data = get_current_weather(city)

    # city is not found by the api
    # if not weather_data['current']['condition']['code'] == 200:
    #     return render_template('city_not_found.html')

    return render_template(
        "weather.html",
        title = 'Pune' if weather_data['location']['name'] == '' else weather_data['location']['name'],
        feels_like = f"{weather_data['current']['feelslike_c']:.1f}",
        calc_on = weather_data['location']['localtime']
    )

if __name__ == '__main__':
    serve(app , host="0.0.0.0", port=8000)