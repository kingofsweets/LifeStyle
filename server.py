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
        
        names = "Спортивный костюм adidas M SERENO TS"
        costs = 6168
        img_links = "https://cdn1.ozone.ru/s3/multimedia-h/wc1200/6099651941.jpg"
        

            
        return {"data":{"name": [names,names,names,names,names,names,names,names,names], "img_link": [img_links,img_links,img_links,img_links,img_links,img_links,img_links,img_links,img_links,img_links],"address": ["lol","lol","lol","lol","lol","lol","lol","lol","lol","lol",], "cost": [costs,costs,costs,costs,costs,costs,costs,costs,costs,costs,]}}
    



if __name__ == "__main__":
    app.run(host="0.0.0.0")