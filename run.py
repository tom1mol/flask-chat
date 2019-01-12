import os     #access environment variables
from datetime import datetime    #import datetime module from datetime library(built in module in python library)
                                    #allows us to work specifically with dates and times
from flask import Flask, redirect, render_template, request, session, url_for        
                        #import redirect module from flask library
                        #render_template. rather than import a string we import this module(relates to index.html)
                        #request module. handle our username form
                        #session module. handle session variables
                        
app = Flask(__name__)                               #initialise new flask app(define flask app)
app.secret_key = os.getenv("SECRET","randomstring123")      #generate session ID using secret_key(random list letters/num/characters)
                                        #generally set it as environment variable. for now is as a string   
                                        #make secret key an environment variable
                    #leave randomstring123 as 2nd arg as it becomes default value if flask cant find var SECRET
messages = []                                       #empty list

def add_message(username, message):        #function that will take username and message and append it to list
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S") #strf method takes date/time obj and converts to a string using given format
                # .now() method used to get current time
                
    
            #dictionary to store message info. store as key value pairs.
            #key= timestamp. value=now(was created on line above)
            
    #messages.append("({}) {}: {}".format(now, username, message)) #append string using format method
    messages.append({"timestamp": now, "from": username, "message": message})

 

    
@app.route('/', methods = ["GET", "POST"])  #root decorator for index page. get and post relates to form in index.html
def index():            #define function that'll be bound to our decorator

    """Main page with instructions"""
    
    if request.method == "POST":    #create new var in session called username
        session["username"] = request.form["username"]  #equal to request.form["username"]
    
    if "username" in session:       #if username exists..redirect to personal chat page
        return redirect(url_for("user", username=session["username"]))    #redirect to contents of session username var
        
    
    #return "To send a message use /USERNAME/MESSAGE"..this one applied to putting username/mess in address bar
    return render_template("index.html")
    
    
    
                                #add abilty to accept post method
@app.route('/chat/<username>', methods = ["GET", "POST"])       #users personalised welcome page
def user(username):             #a function that will bind to the route decorator. argument of username
    """add and display chat messages"""
    #check to see if message has been posted from the form and if so..add to messages list
    #we are obtaining our username and message variables and send them to add_messages function to add to list
    
    if request.method == "POST":                #if this is the case..obtain following variables
        username = session["username"]          #username we get from session variable username
        message = request.form["message"]       #message came from form so is part of request obj
        add_message(username, message)         #call add_messages function ith 2 var we just created(username,mess)
        return redirect(url_for("user", username=session["username"]))    #return redirect to session username
        #if url is changed, we dont have to worry about what redirects might be calling it directly
        #return redirect is needed or else every time the page refreshes the message is repeated(resends post data)
    
    return render_template("chat.html", username = username, chat_messages = messages)
    
    #return "Welcome, {0}: {1}".format(username, messages )          #return to the user hi + username
    #return "<h1>Welcome, {0}</h1>{1}".format(username, messages)
    #welcome message in h1 tags..subsequent message(get-all-messages outside the h1)
    
    
"""   
@app.route('/<username>/<message>')     #dont need this as we are using textbox 
def send_message(username, message):     #function that is binded to decorator. 2 args username and message
        #create a new message and redirect back to the chat page 
    add_messages(username, message)                 #call add_messages function with username/message arguments
    return redirect(username)       #redirect back to users personalised welcome page(above)
"""    
app.run(host=os.getenv('IP', "0.0.0.0"), port=int(os.getenv('PORT', "5000")), debug=False)       #get IP and port
#by setting IP to 0.0.0.0 and port to 5000..we dont have to set them in heroku
#set debug to false as we dont want debug=true to be set in production
    
    
    
    
    
    
    
    