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
        data = pd.read_csv('ozon.csv').to_numpy()
        
        objects = []
        rand = np.random.randint(0, 3000, 9)
        for i in range(9):
            objects.append({"name":str(data[[rand[i]], 0][0]), "img_link":"https://www.ozon.ru" +  str(data[[rand[i]], 3][0]), "address": "test",  "cost": str(data[[rand[i]], 2][0])})
        
        print(objects[0])
        
        return {"data": objects}
    



if __name__ == "__main__":
    app.run(host="0.0.0.0")