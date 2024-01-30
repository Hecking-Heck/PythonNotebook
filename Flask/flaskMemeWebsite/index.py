# Import
from flask import Flask, render_template
import requests
import json

# Using render_template we can create a "templates" folder, any files in there can be served using the
# render_template() function as seen below with "index.html"

# requests is there so we can make Web Requests
# json is there so we can parse JSON

# Create a Flask app
app = Flask(__name__)

# The original meme api went down so now I am using meme-api.com
def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    print(response)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

# Define a route and view function
@app.route('/')
def index():
    meme_pic,subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit), 200

# Run the app
if __name__ == '__main__':
    app.run()