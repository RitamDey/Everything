import os
import sys

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import Firefox


# Set the MOZ_HEADLESS environment variable to cause Firefox be headless
os.environ['MOZ_HEADLESS'] = '1'


# Construct the binary object and use it to start a driver session
driver = Firefox()
driver.get("https://intoli.com/blog/running-selenium-with-headless-firefox/")


heading = driver.find_element_by_xpath("//*[@id='heading-breadcrumbs']")
if heading:
    print(heading.get_property('textContent').strip())
else:
    print("Heading not found")


driver.close()
