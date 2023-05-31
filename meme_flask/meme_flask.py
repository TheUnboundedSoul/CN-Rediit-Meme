from flask import Flask, render_template

import requests
import json

app = Flask(__name__)

def get_meme():
    #
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    postlink = response["postLink"]
    autor = response["author"]
    subreddit = response["subreddit"]
    return meme_large, subreddit, autor, postlink

@app.route("/")

def index():
    meme_pic, subreddit, autor, postlink = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit, autor=autor, postlink=postlink)

app.run(host="0.0.0.0", port=80)