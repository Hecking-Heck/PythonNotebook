# Imports
from flask import Flask, request, render_template

# Variables
pageCounts: int = 0

webServer = Flask(__name__)

# Server routing
@webServer.route('/', methods=['GET'])
def index():
    global pageCounts
    playPage = f""" <DOCTYPE html><html lang="en"> <head><meta charset="UTF-8"> <meta name="viewport"content="width=device-width, initial-scale=1.0"><title>Main Page</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"></head> <body> <div class="container"><div class="jumbotron"><h1 class="display-1"> Hello NAME HERE </h1> <a href="/other">Link to Other Page</a> </div> <p> Page Visited {pageCounts} times.</p> </div></body> </html>"""
    pageCounts = pageCounts + 1
    return playPage

@webServer.route('/other/', methods=['GET'])
def other():
    otherPage = f""" <DOCTYPE html><html lang="en"> <head><meta charset="UTF-8"> <meta name="viewport"content="width=device-width, initial-scale=1.0"><title>Other Page</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"></head> <body> <div class="container"><div class="jumbotron"><h1 class="display-1"> Other Page </h1> <a href="/">Link to Main Page</a> </div> </div></body> </html>"""
    return otherPage

@webServer.route('/play/<name>')
def play(name):
    print(f"Name is {name}")
    playPage = f""" <DOCTYPE html><html lang="en"> <head><meta charset="UTF-8"> <meta name="viewport"content="width=device-width, initial-scale=1.0"><title>Hello {name}</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"></head> <body> <div class="container"><div class="jumbotron"><h1 class="display-1"> Hello {name}</h1> <a href="/">Link to Main Page</a> </div> </div></body> </html>"""
    return playPage

@webServer.route('/doform/', methods=['GET', 'POST'])
def doform():
    name = request.args.get('name')
    print(f"Name is {name}")
    formOutPage = f""" <DOCTYPE html><html lang="en"> <head><meta charset="UTF-8"> <meta name="viewport"content="width=device-width, initial-scale=1.0"><title>FORM= {name}</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"></head> <body> <div class="container"><div class="jumbotron"><h1 class="display-1"> Output was {name}</h1> <a href="/">Link to Main Page</a> </div> </div></body> </html>"""
    return formOutPage

@webServer.route('/form', methods=['GET'])
def form():
    formPage = f""" <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">

        <meta name="viewport" content="width=device-width, initial-
        scale=1.0">

        <title>User Name Form</title>
        </head>
        <body>
        <h2>Enter Your Name</h2>
        <form action="/doform/" method="GET">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Go</button>
        </form>
        </body>
        </html>
    """
    return formPage

@webServer.route('/essay/', methods=['GET'])
def showEssay():
    return render_template('essay.html')

@webServer.route('/signup/', methods=['GET'])
def signup():
    return render_template('signup.html')

@webServer.route('/login/', methods=['GET'])
def login():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    email = request.args.get('email')
    age = request.args.get('age')
    password = request.args.get('password')

    print(f'----\n{fname} {lname} has logged in.\nEmail: {email}\nPassword: {password}\nAge: {age}\n----')

    return render_template('login.html', firstName=fname, lastName=lname, thisEmail=email, thisAge=age, thisPassword=password)

if __name__ == "__main__":
    webServer.run(debug=True)