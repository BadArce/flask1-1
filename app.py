from flask import Flask, jsonify
from random import randint
import requests
from json import load as jload

app = Flask(__name__)

@app.route('/hello')
def hello():
  return '<h1>Hello, World!</h1>'

@app.route('/hello/<name>')
def say_hi(name):
  return f"<h1>Hello {name}</h1>"

@app.route('/hello/<name>/<city>')
def say_hello(name,city):
  return f"<h1>Hello {name}, I didn't know you were from {city}!</h1>"

@app.route('/add/<name>/<age>/<city>/<state>')
def add_user(name,age,city,state):
  name = f"{name}-1"
  age = f"{age}-1"
  city = f"{city}-1"
  state = f"{state}-1"
  user_data = {
    'name': name,
    'age': age,
    'city': city,
    'state': state
  }
  return jsonify(user_data)

@app.route('/random/<start>/<end>')
def random_int(start,end):
  try:
    start = int(start)
    try:
      end = int(end)
    except:
      return "Invalid input!"
  except:
    return "Invalid input!"
  return f"<h1> Your number is: {randint(start,end)}</h1>"
  
@app.route('/quote')
def quote_me():
  response = requests.get("https://zenquotes.io/api/random")
  response = response.json()[0]
  quote = response["q"]
  author = response["a"]
  return f'<div><h1>"{quote}"</h1><h3>-{author}</h3></div>'

@app.route('/get/<search>')
def get_user(search):
  try:
    search = int(search)
  except:
    return "Input Invalid"
  db = open('MOCK_DATA.json')
  data = jload(db)
  found = "User not found"
  for x in data:
    if x["id"] == search:
      found = x
      return found
    

if __name__ == '__main__':
  app.run()

