# A web-scraper made for HypeDC.


# Import the necessary libraries
from bs4 import BeautifulSoup
import requests
import re


# All men's shoes on HypeDC
def menHype():
    # Basic setup
    page = requests.get('https://www.hypedc.com/mens')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Show the connection is successful
    if page.status_code == 200:
        print('Connection successful.\n')
    else:
        print('Connection failed.\n')

    # Shoe brands
    brands = []
    for shoe_brand in soup.find_all('span', class_='brand-name'):
        brands.append(shoe_brand.get_text())

    # Shoe names
    styles = []
    for shoe_name in soup.find_all('h5', class_='product-name h4'):
        styles.append(shoe_name.get_text())

    # Shoe pricing
    prices = []
    for shoe_price in soup.find_all('span', class_='price product-price'):
        prices.append(shoe_price.get_text())

    # Shoe sizing available
    sizes = []
    for shoe_size in soup.find_all('a', href=re.compile('available')):
        print(shoe_size)

    # Print all the information side by side
    shoe_lists = [brands, styles, prices]
    print('All Men`s shoes:')
    for items in zip(*shoe_lists):
        print(*items)


# All women's shoes on HypeDC
def womenHype():
    # Basic setup
    page = requests.get('https://www.hypedc.com/womens')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Show the connection is successful
    if page.status_code == 200:
        print('Connection successful.\n')
    else:
        print('Connection failed.\n')

    # Shoe brands
    brands = []
    for shoe_brand in soup.find_all('span', class_='brand-name'):
        brands.append(shoe_brand.get_text())

    # Shoe names
    styles = []
    for shoe_name in soup.find_all('h5', class_='product-name h4'):
        styles.append(shoe_name.get_text())

    # Shoe pricing
    prices = []
    for shoe_price in soup.find_all('span', class_='price product-price'):
        prices.append(shoe_price.get_text())

    # Shoe sizing available
    sizes = []
    for shoe_size in soup.find_all('a', href=re.compile('available')):
        print(shoe_size)

    # Print all the information side by side
    shoe_lists = [brands, styles, prices]
    print('All Women`s shoes:')
    for items in zip(*shoe_lists):
        print(*items)


# All children shoes on HypeDC
def kidsHype():
    # Basic setup
    page = requests.get('https://www.hypedc.com/kids')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Show the connection is successful
    if page.status_code == 200:
        print('Connection successful.\n')
    else:
        print('Connection failed.\n')

    # Shoe brands
    brands = []
    for shoe_brand in soup.find_all('span', class_='brand-name'):
        brands.append(shoe_brand.get_text())

    # Shoe names
    styles = []
    for shoe_name in soup.find_all('h5', class_='product-name h4'):
        styles.append(shoe_name.get_text())

    # Shoe pricing
    prices = []
    for shoe_price in soup.find_all('span', class_='price product-price'):
        prices.append(shoe_price.get_text())

    # Shoe sizing available
    sizes = []
    for shoe_size in soup.find_all('a', href=re.compile('available')):
        print(shoe_size)

    # Print all the information side by side
    shoe_lists = [brands, styles, prices]
    print('All Children`s shoes:')
    for items in zip(*shoe_lists):
        print(*items)


# All new arrivals on HypeDC
def newOnHype():
    # Basic setup
    page = requests.get('https://www.hypedc.com/new-arrivals')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Show the connection is successful
    if page.status_code == 200:
        print('Connection successful.\n')
    else:
        print('Connection failed.\n')

    # Shoe brands
    brands = []
    for shoe_brand in soup.find_all('span', class_='brand-name'):
        brands.append(shoe_brand.get_text())

    # Shoe names
    styles = []
    for shoe_name in soup.find_all('h5', class_='product-name h4'):
        styles.append(shoe_name.get_text())

    # Shoe pricing
    prices = []
    for shoe_price in soup.find_all('span', class_='price product-price'):
        prices.append(shoe_price.get_text())

    # Shoe sizing available
    sizes = []
    for shoe_size in soup.find_all('a', href=re.compile('available')):
        print(shoe_size)

    # Print all the information side by side
    shoe_lists = [brands, styles, prices]
    print('All New Arrivals on HypeDC:')
    for items in zip(*shoe_lists):
        print(*items)


# All sale items on HypeDC
def saleHype():
    # Basic setup
    page = requests.get('https://www.hypedc.com/sale')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Show the connection is successful
    if page.status_code == 200:
        print('Connection successful.\n')
    else:
        print('Connection failed.\n')

    # Shoe brands
    brands = []
    for shoe_brand in soup.find_all('span', class_='brand-name'):
        brands.append(shoe_brand.get_text())

    # Shoe names
    styles = []
    for shoe_name in soup.find_all('h5', class_='product-name h4'):
        styles.append(shoe_name.get_text())

    # Shoe pricing
    prices = []
    for shoe_price in soup.find_all('span', class_='price product-price'):
        prices.append(shoe_price.get_text())

    # Shoe sizing available
    sizes = []
    for shoe_size in soup.find_all('a', href=re.compile('available')):
        print(shoe_size)

    # Print all the information side by side
    shoe_lists = [brands, styles, prices]
    print('All New Arrivals on HypeDC:')
    for items in zip(*shoe_lists):
        print(*items)


def main():
    which_category = input("What type of products would you like to see?:\n -Men's\n -Women's\n -Kids'\n -Sale\n").lower()
    if which_category == 'men':
        menHype()
    if which_category == 'women':
        womenHype()
    if which_category == 'kid':
        kidsHype()
    if which_category == 'sale':
        saleHype()
    else:
        print("Please choose a category.")
        main()


main()
