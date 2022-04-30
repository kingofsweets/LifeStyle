import requests
import json
import bs4
import fuzzywuzzy
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
    csv_f = open('ozon_1.csv', 'w')
    writer = csv.writer(csv_f)
    
    writer.writerow(["title", "brand", "cost", "link", "sizes"])
    
    page = 2
    
    for page in range(3000):
        sleep(2)
        
        try:
            r = session.get(f'https://www.ozon.ru/category/muzhskaya-odezhda-7542/?page={page}')

            r.html.render()  

            names = r.html.find('.tile-hover-target.i5n > .de0.ed0.de1.e2d.tsBodyL')
            costs = r.html.find('.p1i > .ui-s2')
            links = r.html.find('.tile-hover-target.i5n')
            color = r.html.find('.f6d.df7')
            sizes = r.html.find('.df8.f8d')
            
            print("Всего элементов: " + str(len(names)), str(len(costs)), str(len(links)), str(len(sizes)))
    
            names = [name.text for name in names]
            costs = [cost.text for cost in costs]
            sizes = [size.text for size in sizes]
            links = [link.attrs['href'] for link in links]        
            brands = get_brands(names)
    
    
            for i in range(len(names)):
                writer.writerow([names[i], brands[i], costs[i], links[i], sizes[i]])
        
        except:
            print("Чота не работает...")
    
        
    csv_f.close()
        
pars_clothes()