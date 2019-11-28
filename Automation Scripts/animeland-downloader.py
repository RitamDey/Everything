from selenium.webdriver import Chrome
from sys import argv, exit
from time import sleep
from os import mkdir, chdir


def processEpisode(name, url, browser):
    # Get the episode
    browser.get(url)

    # Make and change to the new directory
    mkdir(name)
    chdir(name)

#TODO: Parse and download the videos
    pass


def main(url):
    with Chrome(executable_path="/home/stux/Downloads/chromedriver") as browser:
        browser.get(f"https://animeland.us/dub/{url}")

        print("Sleeping for 10s to allow site to load fully")
        sleep(10)

        name = browser.find_element_by_xpath("//div[@id='popular_video']/h1").text
        print(f"Downloading {name}")

        episodes = browser.find_elements_by_xpath("//ul[@class='anime-col']/li/a")
        
        for ep in episodes:
            url = ep.get_attribute("href")
            name = ep.text
            print(f"Downloading {name} => {url}")

            processEpisode(name=name, url=url, browser=browser)



if __name__ == "__main__":
    if len(argv) < 2:
        print("Need a anime name")
        exit(-1)
    name = argv[1]
    url = name.lower().replace(" ", "-")
    main(url)
