from flask import render_template
from glob import glob
import random
import os

def home():
   image_list = glob("./app/static/images/*.jpg")
   images = [os.path.basename(i) for i in random.sample(image_list, 3)]
   return render_template('home.html', images=images)
   

def test():
   return "testo"