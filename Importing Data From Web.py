import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""Importing Data From The Web"""

##########
#Method#0# - This is just to make the request, doesn't do anything w/ it
##########

from urllib.request import urlopen, Request

url = 'https://en.wikipedia.org/wiki/Combined_statistical_area'

request = Request(url)

response = urlopen(request)

response.close()



##########
#Method#1# - This READS the request in and saves it locally!
##########

from urllib.request import urlretrieve

url = 'https://en.wikipedia.org/wiki/Combined_statistical_area'

request = Request(url)

response = urlopen(request)

html = response.read()

response.close()

urlretrieve(url, 'us-combined-statistical-areas')



##########
#Method#2#
##########

import requests

url = 'https://en.wikipedia.org/wiki/Combined_statistical_area'
 
r = requests.get(url)

text = r.text



##########
#Method#3#
##########


from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Combined_statistical_area'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

print(soup.prettify())
