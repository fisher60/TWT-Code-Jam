from flask import Flask,request,render_template,redirect, url_for
from Fetch_contents.main_search_topic import *

#from Fetch_contents.main_search_topic import *
import time
app = Flask(__name__)


@app.route('/')
def my_form():
    # try:
    return render_template('form.html')
    # except:
    #     return render_template('404.html')

@app.route('/', methods=['POST'])
def my_form_post():
    # try:
    text = request.form['topic']
    print(text)
    return redirect(url_for('index',topic = text,run="True"))
    # except:
    #     return render_template('404.html')


@app.route('/<topic>/<run>')
def index(topic,run):
    # try:
    if run == "True":
        my_dict = start_fetching(topic)
        run = "False"
        return render_template('testing.html', **my_dict)
    # except:
    #     return render_template('404.html')    

if __name__ == '__main__':
   app.run()

#
