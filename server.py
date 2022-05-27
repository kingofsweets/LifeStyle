from numpy import size
from flask import Flask, request, send_file, send_from_directory
import flask
import os
from base64 import b64encode
from PIL import Image
import io
import pandas as pd
import numpy as np
app = Flask(__name__)

      
@app.route("/", methods=['GET'])
def index():
    return send_from_directory('demo', 'index.html')

@app.route("/clothes", methods = ['GET', 'POST'])
def test_api():
    if request.method == 'GET':
        data = pd.read_csv('ozon.csv')
        
        objects = []
        rand = np.random.randint(0, 3000, 9)
        for i in range(9):
            objects.append({"name":str(data.loc[[rand[i]]]["title"]), "img_link": str(data.loc[[rand[i]]]["link"]), "address": "test",  "cost": str(data.loc[[rand[i]]]["cost"])})
        
        print(objects[0])
        
        return {"data": objects}
    



if __name__ == "__main__":
    app.run(host="0.0.0.0")