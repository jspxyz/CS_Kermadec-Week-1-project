# selecting Tiki products
# Laptops - IT Equipment
# https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=c.1846.hamburger_menu_fly_out_banner
# https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=c.1846.hamburger_menu_fly_out_banner&page=2

# function to import the website and prase the raw text with beautiful soup
# Todo1: need to add for loop to crawl through x pages
# Todo2: add sleep function so Tiki does not kick us out
''' 
import requests
from bs4 import BeautifulSoup

url = 'https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=c.1846.hamburger_menu_fly_out_banner'

def get_url(url):
    """Get parsed HTML from url
      Input: url to the webpage
      Output: Parsed HTML text of the webpage
    """
    # Send GET request
    r = requests.get(url)

    # Parse HTML text
    soup = BeautifulSoup(r.text, 'html.parser')

    return soup
'''
# saving data set for testing
# soup = get_url(url) # this brings the soup variable to a global status
# soup_fortesting = soup

# function to extract information
''' need the following
- data-seller-product-id
- product-sku
- data-title
- data-price
- data-category
- product image
- product link
- discount % price
- original price
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