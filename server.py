from turtle import color

from numpy import size
from flask import Flask, request, send_file, send_from_directory
import flask
import os
from base64 import b64encode
from PIL import Image
import io
app = Flask(__name__)


      
@app.route("/", methods=['GET'])
def index():
    return send_from_directory('demo', 'index.html')

@app.route("/clothes", methods = ['GET', 'POST'])
def test_api():
    if request.method == 'GET':
        return "Hello, you have landed on the lifestyle host api. To interact with the application, use the POST method."
        
    if request.method == 'POST':                                 
        style = request.form['style'] 
        colors = request.form['colors']
        sizes = request.form['sizes']
        print = request.form['print']

        
        
        name = "Спортивный костюм adidas M SERENO TS"
        cost = 6168
        img_link = "https://cdn1.ozone.ru/s3/multimedia-h/wc1200/6099651941.jpg"
        

            
        return {"name": name, "img_link": img_link,"address": "lol", "cost": cost}



if __name__ == "__main__":
    app.run(host="0.0.0.0")