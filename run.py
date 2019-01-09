import os     #access environment variables
from datetime import datetime    #import datetime module from datetime library(built in module in python library)
                                    #allows us to work specifically with dates and times
from flask import Flask, redirect, render_template, request, session        
                        #import redirect module from flask library
                        #render_template. rather than import a string we import this module(relates to index.html)
                        #request module. handle our username form
                        #session module. handle session variables
                        
app = Flask(__name__)                               #initialise new flask app(define flask app)
app.secret_key = "randomstring123"      #generate session ID using secret_key(random list letters/num/characters)
                                        #generally set it as environment variable. for now is as a string            
messages = []                                       #empty list

def add_messages(username, message):        #function that will take username and message and append it to list
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S") #strf method takes date/time obj and converts to a string using given format
                # .now() method used to get current time
                
    messages_dict = {"timestamp": now, "from": username, "message": message}
            #dictionary to store message info. store as key value pairs.
            #key= timestamp. value=now(was created on line above)
            
    #messages.append("({}) {}: {}".format(now, username, message)) #append string using format method
    messages.append(messages_dict)

 

    
@app.route('/', methods = ["GET", "POST"])  #root decorator for index page. get and post relates to form in index.html
def index():            #define function that'll be bound to our decorator

    """Main page with instructions"""
    
    if request.method == "POST":    #create new var in session called username
        session["username"] = request.form["username"]  #equal to request.form["username"]
    
    if "username" in session:       #if username exists..redirect to personal chat page
        return redirect(session["username"])    #redirect to contents of session username var
        
    
    #return "To send a message use /USERNAME/MESSAGE"..this one applied to putting username/mess in address bar
    return render_template("index.html")
    
    
@app.route('/<username>')       #users personalised welcome page
def user(username):             #a function that will bind to the route decorator. argument of username
    """display chat messages"""
    return render_template("chat.html", username = username, chat_messages = messages)
    
    #return "Welcome, {0}: {1}".format(username, messages )          #return to the user hi + username
    #return "<h1>Welcome, {0}</h1>{1}".format(username, messages)
    #welcome message in h1 tags..subsequent message(get-all-messages outside the h1)
    
    
    
@app.route('/<username>/<message>')
def send_message(username, message):     #function that is binded to decorator. 2 args username and message
    """create a new message and redirect back to the chat page """
    add_messages(username, message)                 #call add_messages function with username/message arguments
    return redirect(username)       #redirect back to users personalised welcome page(above)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)             #get IP and port
    
    
    
    
    
    
    
    