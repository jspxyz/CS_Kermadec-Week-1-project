# selecting Tiki products
# Laptops - IT Equipment
# https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=c.1846.hamburger_menu_fly_out_banner
# https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=c.1846.hamburger_menu_fly_out_banner&page=2

# function to import the website
# need to crawl through x pages
# add sleep function
''' example code from class
import requests

r = requests.get('https://vnexpress.net/')

print(r.text)
''''

# function to prase the raw text with beautiful soup
''' example code from class
from bs4 import BeautifulSoup

# r.text is a HTML file so we will use html.parser
soup = BeautifulSoup(r.text, 'html.parser')

'''

# function to extract information
''' need the following
- product ID
- product price
- product image
'''

# function to convert to pandas dataframe
'''
import pandas as pd

articles = pd.DataFrame(data = data, columns = data[0].keys())
'''


# function to store result
'''
articles.to_csv("./result.csv", index=False)
'''