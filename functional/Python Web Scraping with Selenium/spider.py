from selenium import webdriver
import time
import requests
from PIL import Image
from io import BytesIO


# The URL we want to fetch
url = "https://unsplash.com"

# Using Selenium's webdriver to open the page
driver = webdriver.Firefox(executable_path=r'geckodriver')
driver.get(url)


# Scroll page and wait 5 seconds
driver.execute_script("window.scrollTo(0,1000);")
time.sleep(5)


i = 0
# Select image elements and print their URLs
image_elements = driver.find_elements_by_css_selector("#gridMulti img")

for image_element in image_elements:
    image_url = image_element.get_attribute("src")

    # Send a HTTP GET request to get the image
    image_object = requests.get(image_url)
    # Create a BytesIO buffer and use it for opening a Image object
    image = Image.open(BytesIO(image_object.content))

    # Then write it out
    image.save("/home/stux/EarthPorn/images/image"+str(i)+"."+image.format, image.format)
    i += 1

