# import requests
# import json
# import bs4
# import fuzzywuzzy
from requests_html import HTMLSession
import csv
from time import sleep
def cut_brand(name, source):
    brand = "unnamed"
    for s in source:
        if s in name:
            brand = s
    
    return brand

def get_brands(names):
    source = open('brands.txt').readlines()
    source = [line.rstrip() for line in source]

    brands = []
    for name in names:
        brand = cut_brand(name, source)
        brands.append(brand)
    
    return brands
        
    

def pars_clothes():
    session = HTMLSession()
    csv_f = open('ozon_test.csv', 'w')
    writer = csv.writer(csv_f)
    
    writer.writerow(["title", "brand", "cost", "link", "sizes"])
    
    page = 2
    
    for page in range(3000):
        sleep(2)
        
        try:
            r = session.get(f'https://www.ozon.ru/category/muzhskaya-odezhda-7542/?page={page}')

            r.html.render()  

            names = r.html.find('.tile-hover-target.wi0 > .i8d.d9i.i9d.dj1.tsBodyL.wi0')
            costs = r.html.find('.ui-t7')
            links = r.html.find('.tile-hover-target.wi0')
            img_links = r.html.find('.ui-r3')
            sizes = r.html.find('.d6k.dk7')
            
            print("Всего элементов: " + str(len(names)), str(len(costs)), str(len(links)), str(len(sizes)))
    
            names = [name.text for name in names]
            costs = [cost.text for cost in costs]
            sizes = [size.text for size in sizes]
            links = [link.attrs['href'] for link in links]
            img_links = [link.attrs['href'] for link in img_links]  
            brands = get_brands(names)
    
    
            for i in range(len(names)):
                writer.writerow([names[i], brands[i], costs[i], links[i], sizes[i]])
        
        except:
            print("Чота не работает...")
    
        
    csv_f.close()
        
pars_clothes()