from flask import Flask, render_template
import random
import datetime 
from faker import Faker
import requests

app = Flask(__name__)

@app.route('/')

def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num = random_number, year = current_year)

@app.route('/guess/<name>')
def guess(name):

    # api key first 
    api_key = '456e0cea0b6797ddc24720c1847395ea'

    # name 
    random_name = fake.first_name()
    print(random_name)

    # url 
    url = f'https://api.genderize.io?name={random_name}&apikey={api_key}'

    # response 
    response = requests.get(url)
    print(response)
    data = response.json()
    print(data)

    # extracting rest of data
    gender = data.get('gender')
    prob = data.get('probability', 0)
    
    # returing the values to the template
    current_year = datetime.datetime.now().year
    return render_template('guess.html', name  = random_name, gender = gender, probability = prob, year = current_year) 




if __name__ == '__main__':
    app.run(debug=True)
    