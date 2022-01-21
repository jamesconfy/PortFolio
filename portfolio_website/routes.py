from flask import render_template
from portfolio_website import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contacts')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/previous")
def previous():
    return render_template('previous.html', title='Previous Works')