from flask import render_template, url_for, send_file
from flask import current_app as app
#import pdfkit

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

@app.route("/resume")
def getResume():
    resume = "static/assets/James-Confidence-CV.pdf"
#    resume = url_for('static', filename='assets/James-Confidence-CV.pdf')
    return send_file(resume, as_attachment=False)