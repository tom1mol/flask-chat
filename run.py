import os     #access environment variables
from flask import Flask, redirect           #import redirect module from flask library

app = Flask(__name__)                               #initialise new flask app(define flask app)
messages = []                                       #empty list

def add_messages(username, message):        #function that will take username and message and append it to list
    """Add messages to the 'messages' list"""
    messages.append("{}: {}".format(username, message)) #append string using format method
    
    
def get_all_messages():
    """Get all messages and seperate them with a 'br' """
    return "<br>".join(messages)        #join method
    
    
@app.route('/')     #root decorator for index page
def index():            #define function that'll be bound to our decorator

    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"
    
    
@app.route('/<username>')       #users personalised welcome page
def user(username):             #a function that will bind to the route decorator. argument of username
    """display chat messages"""
    #return "Welcome, {0}: {1}".format(username, messages )          #return to the user hi + username
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())
    #welcome message in h1 tags..subsequent message(get-all-messages outside the h1)
@app.route('/<username>/<message>')
def send_message(username, message):     #function that is binded to decorator. 2 args username and message
    """create a new message and redirect back to the chat page """
    add_messages(username, message)                 #call add_messages function with username/message arguments
    return redirect(username)       #redirect back to users personalised welcome page(above)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)             #get IP and port
    
    
    
    
    
    
    
    