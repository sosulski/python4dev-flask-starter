# Programming in Python: Flask starter
# Run this file, then look at the preview pane to see your site.

from flask import Flask, render_template

app = Flask(__name__)


# Each route is a web address on your site.
# When someone visits it, Flask sends back an HTML page from the "templates" folder.

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/help")
def help_page():
    return render_template("help.html")


if __name__ == "__main__":
    # host="0.0.0.0" lets Replit show your app in the preview pane
    app.run(host="0.0.0.0", port=5000, debug=True)
