from flask import Flask, render_template

import pymysql
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

    #database connection
    Connection = pymysql.connect(host="dbmemes.ctykqi2m0z3s.us-east-1.rds.amazonaws.com", user="admin", passwd="admin.123", database="dbmemes", port=3306)
    cursor = Connection.cursor()

    #queries for retrieving all rows
    query = '''insert into meme_db(post_link, subreddit, autor) values('%s', '%s', '%s')''' % (postlink, subreddit, autor)
    cursor.execute(query)
    #commiting the connection the closing it.
    Connection.commit()
    Connection.close()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit, autor=autor, postlink=postlink)

app.run(host="0.0.0.0", port=80)

