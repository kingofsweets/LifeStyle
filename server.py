
from flask import Flask,request, send_from_directory
from base64 import b64encode
from PIL import Image
import io
import random
import pandas as pd
import numpy as np
app = Flask(__name__)
from time import sleep


      
@app.route("/", methods=['GET'])
def index():
    return send_from_directory('demo', 'index.html')

@app.route("/clothes", methods = ['GET', 'POST'])
def test_api():
    if request.method == 'GET':
        data = pd.read_csv('ozon.csv').to_numpy()
        addresess = ['г. Таганрог, пер. Гоголевский, д. 2/2', 'г. Таганрог, ул. Петровская, д. 69',
                     'г. Таганрог, ул. Бакинская, д. 65', 'г. Таганрог, пл. Мира, д. 7', 'г. Таганрог, ул. Фрунзе, д. 11А',
                     'г. Таганрог, ул. Дзержинского, д. 165Б']
        objects = []
        rand = np.random.randint(0, 3000, 9)
        for i in range(9):
            # sleep(2)
            # r = session.get(f'https://www.ozon.ru{data[[rand[i]], 3][0]}')
            
            # print(f'https://www.ozon.ru{data[[rand[i]], 3][0]}')
            # r.html.render()
            # img_link = r.html.find('[href]')
            seed = random.randint(0, 4)
            
            
            objects.append({"name":str(data[[rand[i]], 0][0]), "img_link":'https://cdn1.ozone.ru/s3/multimedia-h/wc500/6160404569.jpg', "address": addresess[seed],  "cost": str(data[[rand[i]], 2][0]).split('₽')[0] + '₽'})
        
        print(objects[0])
        
        return {"data": objects}
    



if __name__ == "__main__":
    app.run(host="0.0.0.0")