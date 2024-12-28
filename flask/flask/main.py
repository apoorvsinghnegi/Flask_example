from flask import Flask,render_template

###WSGI APPLICATION
app = Flask(__name__) #it creates an instance of Flask class which is our WSGI(web server gateway interface) application.
#__name__ this tells we need to jump there, entry point of our application

@app.route("/") #"/" it means this will become our home page, when we will hit our url with "/", it will go to the app.route decorator
#and then inside this decorator this def function will be called
def welcome():
  return "Welcome to this Flask course. this is amazing course"

@app.route("/index") 
def index():
  return render_template("index.html") #this will send the flow of the code to the templates folder and inside that it will go to
#the index.html page.

@app.route("/about")
def about():
  return render_template("about.html") #this will send the flow of the code to about.html

if __name__ == '__main__':#this is the entry point of any .py file and from here our execution will start
  app.run(debug=True)
  #using debug = true, it means once we are making any changes inside welcome function we dont need to rerun app.py from terminal
  #it would start by itself once we save the file.