# selecting Tiki products
# Laptops - IT Equipment
# https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=c.1846.hamburger_menu_fly_out_banner
# https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=c.1846.hamburger_menu_fly_out_banner&page=2

# function to import the website and prase the raw text with beautiful soup
# Todo1: need to add for loop to crawl through x pages
# Todo2: add sleep function so Tiki does not kick us out

# imports
import requests
from bs4 import BeautifulSoup

# defining our url to start
# will be crawling for Laptops - IT equipment
url = 'https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=c.1846.hamburger_menu_fly_out_banner'

# get url function
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
'''

# function to extract information
def scrape_tiki(url):
    """
    Scrape the Tiki page for Laptop - IT equipment
    Input: url to the page 1 of Tiki category to scrape
    Output: a list containing scraped data of all products
    """

    # get parsed HTML
    soup = get_url(url)

    # find div class 'product-box-list' that lists all products on page
    # this holds products on page
    product_list = soup.find('div',{'class':'product-box-list'})
    
    # get list of all div class 'product-item'
    product_items_div = product_list.find_all('div',{'class':'product-item'})

    # Defining list containing data of all products
    # Will use to append dicionaries
    data = []

    # Loop to go through list of products on page and return a dictionary to append to data list
    for i in range(len(product_items_div)):
        dictionary = {'seller-product-id':'', 'sku':'', 'title':'', 'price':'', 'product-id':'', 'brand':'', 'category':''}
        # We use the try-except blocks to handle errors
        try:
            dictionary['seller-product-id'] = product_items_div[i]['data-seller-product-id']  # in dictionary: seller-product-id
            dictionary['sku'] = product_items_div[i]['product-sku']                           # in dictionary: sku
            dictionary['title'] = product_items_div[i]['data-title']                          # in dictionary: title
            dictionary['price'] = product_items_div[i]['data-price']                          # in dictionary: price
            dictionary['product-id'] = product_items_div[i]['data-id']                        # in dictionary: product-id
            dictionary['brand'] = product_items_div[i]['data-brand']                          # in dictionary: brand
            dictionary['category'] = product_items_div[i]['data-category']                    # in dictioanry: category

            # Append the dictionary to data list
            data.append(dictionary)
        
        except:
            # Skip if error and print error message
            print("We got one article error!")

''' need the following
- product image
- product link
- discount % price?
- original price?
'''

# convert to pandas dataframe
import pandas as pd

productData = pd.DataFrame(data = data, columns = data[0].keys())

# function to store result
'''
articles.to_csv("./result.csv", index=False)
'''