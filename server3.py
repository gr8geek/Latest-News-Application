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

@app.route("/",methods  = ["GET","POST"])
def get_news():
    if request.method == "POST":
        pub = request.form.get("pub")
        if pub=='':
                feed = feedparser.parse(feeds['ndtv'])
                pub = "ndtv"
                return render_template("news.html",channel = pub.upper()+" NEWS", news = feed["entries"])


        pub = pub.lower()
        if feeds[pub]:
                feed = feedparser.parse(feeds[pub])
                return render_template("news.html",channel = pub.upper()+" NEWS", news = feed["entries"])
        return "<h1>Not Found</h1>"
    if request.method =="GET":
        print("---------get method -----------")
        pub = request.args.get("publication")
        if pub==None:
            feed = feedparser.parse(feeds['ndtv'])
            pub = 'ndtv'
        else:
            feed = feedparser.parse(feeds[pub.lower()])
        return render_template("news.html",channel = pub.upper()+" NEWS", news = feed["entries"])
        pub = pub.lower()
        if feeds[pub]:
                feed = feedparser.parse(feeds[pub])
                return render_template("news.html",channel = pub.upper()+" NEWS", news = feed["entries"])
        return "<h1>Not Found</h1>"

app.run(debug=True)