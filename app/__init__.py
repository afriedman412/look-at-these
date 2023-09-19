from flask import Flask, render_template
from .routes import home, test

app = Flask(__name__)

app.route("/")(home)
app.route("/test")(test)