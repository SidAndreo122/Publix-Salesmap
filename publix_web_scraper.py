from bs4 import BeautifulSoup
import requests
import lxml


# source = requests.get('https://www.publix.com/savings/weekly-ad/grocery').text
#
# soup = BeautifulSoup(source, 'lxml')
#
# body = soup.find_all("span")
# print(body)
# products = body.text
# print(products)





# If the actual HTML structure is different, you'll need to adjust the selector






from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

# to keep the browser open after the program finishes
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options) # will know to work with the chrome browser driver
# driver.get("https://www.publix.com/savings/weekly-ad/grocery")
#
# # Wait for JavaScript to load content
# time.sleep(10)  # Adjust sleep time as necessary
#
# while True:
#     try:
#         load_more_button = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[6]/div/div[2]/div[2]/div[4]/button/span')  # Adjust the selector
#         load_more_button.click()
#         time.sleep(5)  # Give time for new products to load
#     except:
#         print("No more 'Load More' button or an error occurred.")
#         print("-----------------------------------------------")
#         break
# # Extract product names
# # Adjust selector based on actual page structure
# product_elements = driver.find_elements(By.CSS_SELECTOR, 'span.p-text.paragraph-md.normal.context--default.color--null.line-clamp.title')
#
# product_list = []
#
# # Print product names
# for product in product_elements:
#     product_name = product.text.strip()
#     if "paper coupon" not in product_name.lower():
#         product_list.append(product_name)
#
# data = pd.DataFrame(product_list, columns=['Product Name'])
#
# data.to_csv('grocery.csv', index=False, encoding='utf-8')

# ----------------------------------------------------------------------------

driver.get("https://www.publix.com/savings/weekly-ad/dairy")

# Wait for JavaScript to load content
time.sleep(10)  # Adjust sleep time as necessary

while True:
    try:
        load_more_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div/div[2]/div[2]/div[4]/button/span')  # Adjust the selector
        load_more_button.click()
        time.sleep(5)  # Give time for new products to load
    except:
        print("No more 'Load More' button or an error occurred.")
        print("-----------------------------------------------")
        break
# Extract product names
# Adjust selector based on actual page structure
product_elements = driver.find_elements(By.CSS_SELECTOR, 'span.p-text.paragraph-md.normal.context--default.color--null.line-clamp.title')

product_list = []

# Print product names
for product in product_elements:
    product_name = product.text.strip()
    if "paper coupon" not in product_name.lower():
        product_list.append(product_name)

data = pd.DataFrame(product_list, columns=['Product Name'])

data.to_csv('dairy.csv', index=False, encoding='utf-8')



driver.get("https://www.publix.com/savings/weekly-ad/beer-and-wine")

# Wait for JavaScript to load content
time.sleep(10)  # Adjust sleep time as necessary

while True:
    try:
        load_more_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[5]/div/div[2]/div[2]/div[4]/button/span')  # Adjust the selector
        load_more_button.click()
        time.sleep(5)  # Give time for new products to load
    except:
        print("No more 'Load More' button or an error occurred.")
        print("-----------------------------------------------")
        break
# Extract product names
# Adjust selector based on actual page structure
product_elements = driver.find_elements(By.CSS_SELECTOR, 'span.p-text.paragraph-md.normal.context--default.color--null.line-clamp.title')

product_list = []

# Print product names
for product in product_elements:
    product_name = product.text.strip()
    if "paper coupon" not in product_name.lower():
        product_list.append(product_name)

data = pd.DataFrame(product_list, columns=['Product Name'])

data.to_csv('beer.csv', index=False, encoding='utf-8')



driver.get("https://www.publix.com/savings/weekly-ad/non-foods")

# Wait for JavaScript to load content
time.sleep(10)  # Adjust sleep time as necessary

while True:
    try:
        load_more_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div/div[2]/div[2]/div[4]/button/span')  # Adjust the selector
        load_more_button.click()
        time.sleep(5)  # Give time for new products to load
    except:
        print("No more 'Load More' button or an error occurred.")
        print("-----------------------------------------------")
        break
# Extract product names
# Adjust selector based on actual page structure
product_elements = driver.find_elements(By.CSS_SELECTOR, 'span.p-text.paragraph-md.normal.context--default.color--null.line-clamp.title')

product_list = []

# Print product names
for product in product_elements:
    product_name = product.text.strip()
    if "paper coupon" not in product_name.lower():
        product_list.append(product_name)

data = pd.DataFrame(product_list, columns=['Product Name'])

data.to_csv('non-foods.csv', index=False, encoding='utf-8')



driver.get("https://www.publix.com/savings/weekly-ad/frozen-food")

# Wait for JavaScript to load content
time.sleep(10)  # Adjust sleep time as necessary

while True:
    try:
        load_more_button = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div/div[2]/div[2]/div[4]/button/span')  # Adjust the selector
        load_more_button.click()
        time.sleep(5)  # Give time for new products to load
    except:
        print("No more 'Load More' button or an error occurred.")
        print("-----------------------------------------------")
        break
# Extract product names
# Adjust selector based on actual page structure
product_elements = driver.find_elements(By.CSS_SELECTOR, 'span.p-text.paragraph-md.normal.context--default.color--null.line-clamp.title')

product_list = []

# Print product names
for product in product_elements:
    product_name = product.text.strip()
    if "paper coupon" not in product_name.lower():
        product_list.append(product_name)

data = pd.DataFrame(product_list, columns=['Product Name'])

data.to_csv('frozen.csv', index=False, encoding='utf-8')


driver.quit()



