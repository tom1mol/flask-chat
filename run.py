import os     #access environment variables
from flask import Flask

app = Flask(__name__)       #initialise new flask app(define flask app)
messages = []       #empty list

def add_messages(username, message):        #function that will take username and message and append it to list
    messages.append("{}: {}".format(username, message)) #append string using format method

@app.route('/')     #root decorator for index page
def index():            #define function that'll be bound to our decorator

    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"
    
    
@app.route('/<username>')       #this gets treated as a variable(username)
def user(username):             #a function that will bind to the route decorator. argument of username
    """display chat messages"""
    #return "Welcome, {0}: {1}".format(username, messages )          #return to the user hi + username
    return "Welcome {0}".format(username, messages)
    
@app.route('/<username>/<message>')
def send_message(username, message):     #function that is binded to decorator. 2 args username and message
    """create a new message and redirect back to the chat page """
    return "{0}: {1}".format(username, message)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)             #get IP and port
    