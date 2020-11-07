import feedparser
from flask import Flask, render_template
app = Flask(__name__)
#Flask Application set

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
NDTV = "https://feeds.feedburner.com/ndtvnews-world-news"
ZEE_NEWS = "https://zeenews.india.com/rss/india-national-news.xml"
feeds = {
    "bbc":BBC_FEED,
    "ndtv":NDTV,
    "zee":ZEE_NEWS
}

@app.route("/")
@app.route("/zee")
def get_news_zee():
    feed = feedparser.parse(ZEE_NEWS)
    return render_template("news.html",channel = "ZEE NEWS", news = feed["entries"])
@app.route("/ndtv")
def get_news_ndtv():
    feed = feedparser.parse(NDTV)
    return render_template("news.html",channel = "NDTV NEWS", news = feed["entries"])
@app.route("/bbc")
def get_news_bbc():
    feed = feedparser.parse(BBC_FEED)
    return render_template("news.html",channel = "BBC NEWS", news = feed["entries"])

app.run(debug=True)