import os     #access environment variables
from flask import Flask

app = Flask(__name__)       #initialise new flask app

@app.route('/')     #root decorator for index page
def index():            #define function that'll be bound to our decorator
    return "<h1>Hello There!</h1>"
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)             #get IP and port
    