from selenium.webdriver import Chrome
from sys import argv, exit
from time import sleep
from os import mkdir, chdir, path
from subprocess import call


def processEpisode(urls):
    # Get the episode
    browser = Chrome(executable_path="/home/stux/Downloads/chromedriver")

    for ep in urls:
        name = ep
        url = urls[ep]
        browser.get(url)

        sleep(10)

        # Make and change to the new directory
        link = browser.find_element_by_xpath("//div[@style='float:right;'][2]/a").get_attribute("href")
        
        print(f"{name} => {link}")
        sleep(5)

        call(["wget", "header=", "-O", name + ".mp4", link])

 

def main(url):
    with Chrome(executable_path="/home/stux/Downloads/chromedriver") as browser:
        browser.get(f"https://animeland.us/dub/{url}")

        print("Sleeping for 10s to allow site to load fully")
        sleep(10)

        name = browser.find_element_by_xpath("//div[@id='popular_video']/h1").text
        print(f"Downloading {name}")

        # Create the anime directory and cd into it
        if path.isdir(name) == False:
            mkdir(name)
        chdir(name)

        episodes = browser.find_elements_by_xpath("//ul[@class='anime-col']/li/a")
        episodes = {ep.text: ep.get_attribute("href") for ep in episodes}

        processEpisode(episodes)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Need a anime name")
        exit(-1)
    name = argv[1]
    url = name.lower().replace(" ", "-")
    main(url)
