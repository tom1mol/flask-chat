import os     #access environment variables
from flask import Flask

app = Flask(__name__)       #initialise new flask app

@app.route('/')     #root decorator for index page
def index():            #define function that'll be bound to our decorator

    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"
    
    
@app.route('/<username>')       #this gets treated as a variable(username)
def user(username):             #a function that will bind to the route decorator. argument of username
    return "Hi " + username          #return to the user hi + username
    
    
@app.route('/<username>/<message>')
def send_message(username, message):     #function that is binded to decorator. 2 args username and message
    return "{0}: {1}".format(username, message)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)             #get IP and port
    