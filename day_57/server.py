from flask import Flask, render_template
import random
import datetime 
from faker import Faker

app = Flask(__name__)

@app.route('/')

def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num = random_number, year = current_year)

def guess():
    api_key = '456e0cea0b6797ddc24720c1847395ea'
    name = Faker().name()
    url = 'https://api.genderize.io?name=peter&apikey={api_key}'
    response = requests.get(url)
    



if __name__ == '__main__':
    app.run(debug=True)
    