from flask import Flask, render_template

# Using render_template we can create a "templates" folder, any files in there can be served using the
# render_template() function as seen below with "index.html"

# Create a Flask app
app = Flask(__name__)

# Define a route and view function
@app.route('/')
def hello_world():
    return render_template("index.html")

# Run the app
if __name__ == '__main__':
    app.run()