import feedparser
from flask import Flask, render_template,request
app = Flask(__name__)
#Flask Application set

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
NDTV = "https://feeds.feedburner.com/ndtvnews-world-news"
ZEE_NEWS = "https://zeenews.india.com/rss/india-national-news.xml"

@app.route("/bbc")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    listnews = """
        <nav style="background:blue">

    <h1>BBC headlines</h1>
    <a href="/bbc">BBC</a>
    <a href="/ndtv">NDV</a>
    <a href="/zee">ZEE news</a>

    </nav>"""
    #print(feed['entries'][0].title)#title, published , summary, link
    for i in feed["entries"]:
        listnews+="""
            <h1>{3}</h1>
    <h3><i>Published At: {0}</i><h3>
    <p ><a href={1}>{2}</a></p>
    <br>
        """.format(i.published,i.link,i.summary,i.title)
    return listnews
@app.route("/")
@app.route("/zee")
def get_news_zee():
    feed = feedparser.parse(ZEE_NEWS)
    listnews = """
        <nav style="background:blue">

    <h1>ZEE news headlines</h1>
    <a href="/bbc">BBC</a>
    <a href="/ndtv">NDV</a>
    <a href="/zee">ZEE news</a>

    </nav>"""
    #print(feed['entries'][0].title)#title, published , summary, link
    for i in feed["entries"]:
        listnews+="""
            <h1>{3}</h1>
    <h3><i>Published At: {0}</i><h3>
    <p ><a href={1}>{2}</a></p>
    <br>
        """.format(i.published,i.link,i.summary,i.title)
    return listnews
@app.route("/ndtv")
def get_news_ndtv():
    feed = feedparser.parse(NDTV)
    listnews = """
        <nav style="background:blue">

    <h1>NDTV headlines</h1>
    <a href="/bbc">BBC</a>
    <a href="/ndtv">NDV</a>
    <a href="/zee">ZEE news</a>

    </nav>"""
    #print(feed['entries'][0].title)#title, published , summary, link
    for i in feed["entries"]:
        listnews+="""
            <h1>{3}</h1>
    <h3><i>Published At: {0}</i><h3>
    <p ><a href={1}>{2}</a></p>
    <br>
        """.format(i.published,i.link,i.summary,i.title)
    return listnews

app.run(debug=True)