from flask import Flask, render_template, request, redirect, url_for
import random
import datetime 
from faker import Faker
import requests

app = Flask(__name__)
fake = Faker()

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        return redirect(url_for('guess', name = user_name))
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num = random_number, year = current_year)

@app.route('/guess/<name>')
def guess(name):

    # url 
    #url = f'https://api.genderize.io?name={random_name}&apikey={api_key}'
    url = f'https://api.genderize.io?name={name}'
    age_url = f'https://api.agify.io?name={name}'
    nationality_url = f'https://api.nationalize.io/?name={name}'

    # response 
    response = requests.get(url)
    data = response.json()
    age_response = requests.get(age_url)
    age_data = age_response.json()
    nationality_response = requests.get(nationality_url)
    nationality_data = nationality_response.json()

    # extracting rest of data
    gender = data.get('gender')
    age = age_data.get('age')
    prob = data.get('probability', 0)

    countries = nationality_data.get('country', [])
    if countries:
        nation = countries[0].get('country_id')
    else:
        nation = 'Unknown'
    
    # returing the values to the template
    current_year = datetime.datetime.now().year
    return render_template('guess.html', name  = name, gender = gender, age = age, nationality = nation, probability = prob, year = current_year) 




if __name__ == '__main__':
    app.run(debug=True)
    