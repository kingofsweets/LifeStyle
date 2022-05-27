
from flask import Flask,request, send_from_directory
from base64 import b64encode
from PIL import Image
import io
import random
import pandas as pd
import numpy as np
app = Flask(__name__)
from time import sleep

dataf = [
    {
        "name":'Рубашка Koton',
        "img_link": 'https://cdn1.ozone.ru/s3/multimedia-5/wc1200/6264553745.jpg',
        "cost": '809₽',
        "address": 'г. Таганрог, пер. Гоголевский, д. 2/2'
    },
    {
        "name":'Брюки ТИМ - модная одежда',
        "img_link": 'https://cdn1.ozone.ru/s3/multimedia-w/wc1200/6287253896.jpg',
        "cost": '790₽',
        "address": 'г. Таганрог, пл. Мира, д. 7'
    },
    {
        "name":'Кеды X-Plode',
        "img_link": 'https://cdn1.ozone.ru/s3/multimedia-a/wc1200/6331868350.jpg',
        "cost": '1499₽',
        "address": 'г. Таганрог, пер. Гоголевский, д. 2/2'
    },
    {
        "name":"Рубашка O'STIN",
        "img_link": 'https://cdn1.ozone.ru/s3/multimedia-u/wc1200/6081431094.jpg',
        "cost": '998₽',
        "address": 'г. Таганрог, ул. Бакинская, д. 65'
    },
    {
        "name":'Классические мужские брюки',
        "img_link": 'https://cdn1.ozone.ru/s3/multimedia-u/wc1200/6119307306.jpg',
        "cost": '2460₽',
        "address": 'г. Таганрог, пл. Мира, д. 7'
    },
    {
        "name":'Кеды X-Plode',
        "img_link": 'https://cdn1.ozone.ru/s3/multimedia-a/wc1200/6331868350.jpg',
        "cost": '1499₽',
        "address": 'г. Таганрог, пер. Гоголевский, д. 2/2'
    },
    {
        "name":"Рубашка Tudors",
        "img_link": 'https://cdn1.ozone.ru/s3/multimedia-g/wc1200/6265232392.jpg',
        "cost": '1422₽',
        "address": 'г. Таганрог, ул. Бакинская, д. 65'
    },
    {
        "name":'Брюки Modis',
        "img_link": 'https://cdn1.ozone.ru/s3/multimedia-s/wc1200/6289571068.jpg',
        "cost": '1299₽',
        "address": 'г. Таганрог, пл. Мира, д. 7'
    },
    {
        "name":'Полуботинки Forum99',
        "img_link": 'https://cdn1.ozone.ru/s3/multimedia-n/wc1200/6280715639.jpg',
        "cost": '4199₽',
        "address": 'г. Таганрог, ул. Бакинская, д. 65'
    }
    
]


      
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
        
        return {"data": dataf}
    



if __name__ == "__main__":
    app.run(host="0.0.0.0")