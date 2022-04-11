# https://vercel.com/docs/runtimes#advanced-usage/advanced-python-usage

from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p> testin HTML : /%s</p>" % (path), mimetype="text/html")