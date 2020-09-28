# selecting Tiki products
# Laptops - IT Equipment
# https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=c.1846.hamburger_menu_fly_out_banner&page=

# function to import the website and prase the raw text with beautiful soup
# Todo1: need to add for loop to crawl through x pages
# Todo2: add sleep function so Tiki does not kick us out

# imports
import requests, random, time
from bs4 import BeautifulSoup
import pandas as pd

# global variables
URL = 'https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=c.1846.hamburger_menu_fly_out_banner&page=' # defining our url to start, searching for Laptops

# function to take url and convert to beautifulsoup data
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

# function to extract information
def scrape_tiki(soup):
    """
    Scrape the Tiki page for Laptop - IT equipment
    Input: url to the page 1 of Tiki category to scrape
    Output: a list containing scraped data of all products
    """

    # get parsed HTML
    # soup = get_url(url)

    # find div class 'product-box-list' that lists all products on page
    # this holds products on page
    product_list = soup.find('div',{'class':'product-box-list'})
    
    # get list of all div class 'product-item'
    product_items_div = product_list.find_all('div',{'class':'product-item'})

    # get length of returned list
    product_items_div_length = len(product_items_div)

    # Defining list containing data of all products
    # Will use to append dicionaries
    data = []

    # Loop to go through list of products on page and return a dictionary to append to data list
    for i in range(len(product_items_div)):
        dictionary = {'seller-product-id':'', 
                        'sku':'',
                        'title':'',
                        'price':'', 
                        'product-id':'', 
                        'brand':'', 
                        'category':'', 
                        'product_link':'',
                        'img_link':'',
                        'original_price':'',
                        'discount':'',
                        'refund':'',
                        'Tiki_now':'',
                        'comment_count':''}
        # We use the try-except blocks to handle errors
        try:
            dictionary['seller-product-id'] = product_items_div[i]['data-seller-product-id']  # in dictionary: seller-product-id
            dictionary['sku'] = product_items_div[i]['product-sku']                           # in dictionary: sku
            dictionary['title'] = product_items_div[i]['data-title']                          # in dictionary: title
            dictionary['price'] = product_items_div[i]['data-price']                          # in dictionary: price
            dictionary['product-id'] = product_items_div[i]['data-id']                        # in dictionary: product-id
            dictionary['brand'] = product_items_div[i]['data-brand']                          # in dictionary: brand
            dictionary['category'] = product_items_div[i]['data-category']                    # in dictioanry: category
            # pulling information from level below div with different tags
            dictionary['product_link'] = product_items_div[i].a['href']                       # in dictionary: product_link
            dictionary['img_link'] = product_items_div[i].img['src']                          # in dictionary: img_link


            # Append the dictionary to data list
            data.append(dictionary)
        
        except:
            # Skip if error and print error message
            print("We got one article error!")

    return data, product_items_div_length

###repeat crawl function through multiple pages
def repeatCrawl(url):
    """
    continue repeating functions get_url & crawlTiki
    until div class product-box-list does not appear
    append data list to one major list
    IMPORTANT : INSERT SLEEP FUNCTION
    """
    product_items_div_length_Loop = 1
    i = 1

    while product_items_div_length_Loop != 0:
        path = url + str(i)
        print(path) # to print path while loop is running to make sure that something is happening
        soupLoop = get_url(path)
        dataLoop, product_items_div_length_Loop = scrape_tiki(soupLoop)
        print(product_items_div_length_Loop) # another check to see the output of each page
        finalData.extend(dataLoop)
        i+=1
        time.sleep(random.randint(2,4))
    
    return finalData

finalData = [] # used in repeatCrawl function to capture all data
finalResult = repeatCrawl(URL)

# for debugging
# print(len(finalResult))
# print(finalResult[0])

# convert to pandas dataframe
dataPrint = pd.DataFrame(data = finalResult, columns = finalResult[0].keys())

# line to store result as csv
dataPrint.to_csv("result.csv", index=False)
