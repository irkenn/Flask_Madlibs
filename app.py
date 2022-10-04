from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route("/")
def home():
    """This will take the prompts from the story Class
    and create a form with it"""
    
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)
