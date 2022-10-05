from distutils.log import debug
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import new_story


app = Flask(__name__)
app.config['SECRET_KEY'] = "there'sNoSpoon"
debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    """This will take the prompts from the story Class
    and create a form with it"""
 
    return render_template("home.html", prompts=new_story.prompts)

@app.route("/story")
def story():
    """This will show the story template and the answers given 
    by the user for each story class prompt"""

    template = new_story.template
    for value in request.args:
        replace_word = request.args.get(value)
        value = '{'+value+'}'
        template = template.replace(value, replace_word)
    return render_template("story.html", templ=template)

