from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route and view function
@app.route('/')
def hello_world():
    return 'Hello World!'

# Run the app
if __name__ == '__main__':
    app.run()