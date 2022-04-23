from unicodedata import name
from regex import F
import requests
import json
import bs4
import fuzzywuzzy
from requests_html import HTMLSession

def pars_clothes():
    session = HTMLSession()

    r = session.get('https://www.ozon.ru/category/bryuki-muzhskie-7552/')

    r.html.render()  

    names = r.html.find('.de0.ed0.de1.e2d.tsBodyL.i5m')
    cost = r.html.find('.ui-s5.ui-s8.ui-t0')
    color = r.html.find('.f6d.df7')
    
    print(len(names), len(cost), len(color))
    
    # f = open('dota.html', 'w', encoding="utf-8").write(str(elements))
    
pars_clothes()