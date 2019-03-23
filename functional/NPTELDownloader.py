from selenium.webdriver import Firefox
from subprocess import call


videos = {}


with Firefox(firefox_binary="/home/stux/Downloads/firefox-dev/firefox-bin") as browser:
    browser.get("https://nptel.ac.in/courses/nptel_download.php?subjectid=106105172")

    table_xpath = "//tbody/tr"
    entry_xpath = "./td[3]/a"
    name_xpath = "./td[2]"
    pdf_xpath = "./td[7]/a"

    for entry in browser.find_elements_by_xpath(table_xpath):
        name = entry.find_element_by_xpath(name_xpath).text
        href = entry.find_element_by_xpath(entry_xpath).get_attribute("href")
        pdf = entry.find_element_by_xpath(pdf_xpath).get_attribute("href")
        videos[name+".mp4"] = [href, pdf]


for vid in videos:
    print(f"Downloading {vid}")
    
    call(["/usr/bin/wget", "-O", vid, videos[vid][0]])
    call(["/usr/bin/wget", videos[vid][1]])

