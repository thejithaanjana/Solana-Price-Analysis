#import json
#import datetime
from ast import parse
from ftplib import parse150
from pprint import pprint
from xml.etree.ElementTree import tostring
from xmlrpc.client import DateTime
import requests 
import bs4 
import lxml
from bs4 import BeautifulSoup
from datetime import datetime
from pyrebase import pyrebase


def parsePrice():
	r = requests.get("https://www.coindesk.com/price/solana/")
	soup = bs4.BeautifulSoup(r.text, 'html')
	price = soup.find_all('span', {'class' : 'typography__StyledTypography-owin6q-0 ktzuAh'})[0].text
	return price

datetime = str(datetime.now())

print(str(parsePrice()))

print(datetime)


config = {
	"apiKey" : "AIzaSyDI8vwvPtEqdRjn2J4WTT-PUwLCFOySFkY",
  "authDomain": "solanapricedatabase.firebaseapp.com",
  "databaseURL": "https://solanapricedatabase-default-rtdb.firebaseio.com",
  "projectId": "solanapricedatabase",
  "storageBucket": "solanapricedatabase.appspot.com",
  "dataBaseUrl" : "https://solanapricedatabase-default-rtdb.firebaseio.com/",
  "messagingSenderId": "950473679159",
  "appId": "1:950473679159:web:ec8045fb91394ad3c37ab2",
  "measurementId": "G-C9C8J2L8K4"
		}

firebase = pyrebase.initialize_app(config) 
database = firebase.database()

data = {
	"datetime" : datetime,
	"price" : parsePrice()
	}

database.push(data)




