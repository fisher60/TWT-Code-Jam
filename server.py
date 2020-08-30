from flask import Flask,request,render_template,redirect, url_for
from Fetch_contents.main_search_topic import *
#from Fetch_contents.main_search_topic import *
import time
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')



@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['topic']
    print(text)
    return redirect(url_for('index',topic = text,run="True"))


@app.route('/<topic>/<run>')
def index(topic,run):
    if run == "True":
        my_dict = start_fetching(topic)
        run = "False"
        return render_template('testing.html',**my_dict)

if __name__ == '__main__':
   app.run()

#
