import feedparser
from flask import Flask, render_template,request
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
def get_news():
    pub = request.args.get("publication")
    if pub==None:
        return "<h1>Not Found</h1>"

    pub = pub.lower()
    if feeds[pub]:
            feed = feedparser.parse(feeds[pub])
            return render_template("news.html",channel = pub.upper()+" NEWS", news = feed["entries"])
    return "<h1>Not Found</h1>"

app.run(debug=True)