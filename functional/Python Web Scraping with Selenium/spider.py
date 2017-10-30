from selenium import webdriver
import time


# The URL we want to fetch
url = "https://unsplash.com"

# Using Selenium's webdriver to open the page
driver = webdriver.Firefox(executable_path=r'geckodriver')
driver.get(url)


# Scroll page and wait 5 seconds
driver.execute_script("window.scrollTo(0,1000);")
time.sleep(5)


# Select image elements and print their URLs
image_elements = driver.find_elements_by_css_selector("#gridMulti img")

for image_element in image_elements:
    image_url = image_element.get_attribute("src")
    print(image_url)
