from flask import Flask,render_template,request,redirect,session
from db import Database
import api

app = Flask(__name__)

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

#sabse phle /register jab ham dalenge toh /register pe jayega uske baad, vo register.html ko kholega
#phir register.html se jab subit button hoga toh anchor tag use kara hai jo ek naye url /perform_registration pe jayega
#phir vo saare parameters vaha se nikalega jaise name, email,password phir in teeno parameters ko .insert use karega jo
#db.py ke andar present hai, jo uske andar users.json file ko open karega jo uska data users karke ek variable mai daalega
#jisse ham dekhenge ki vo email present hai ki nahi .json file mai. Agar present hai toh usme daal dega varna error message print kardega
#jab bhi hum kissi site pe login karte hai toh session use karte hai taaki hame pata rahe ki jo logged in user hai wahi use kar raha
#hai i.e. ussi ka session hai yeh vala
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration',methods=['post'])#method ==post written kyuki hame batana hai ki data post ke through aa raha hai
def perform_registration():
    #name,password,email--> these things we will get from HTML file
    name = request.form.get('user_ka_name') 
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html',message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html',message="Email already exists")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email/password')

@app.route('/profile')
def profile():#directly if session karke dekh rahe hai ki uski value 1 set huyi hai ki nahi
    if session: #iska matlab hai ki session ki value kya hogi, agar 1hai toh he ueh call hoga varna dubara se login page pe bhej diya jayega
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['post'])#kyuki ner perform karne ke liye ham isko data denge toh hamne post use karlia
def perform_ner():
    if session:
        text = request.form.get('ner_text')
        response = api.ner(text)
        print(response)


        return render_template('ner.html',response=response)
    else:
        return redirect('/')

app.run(debug=True)