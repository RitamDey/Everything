from selenium.webdriver import Chrome
from sys import argv, exit
from time import sleep
from os import mkdir, chdir
from os import path


def waitUntilDownloadCompleted(driver, maxTime=600):
    # Download wait function, copied from stackoverflow: https://stackoverflow.com/a/56569251
    driver.execute_script("window.open()")
    # switch to new tab
    driver.switch_to.window(driver.window_handles[-1])
    # navigate to chrome downloads
    driver.get('chrome://downloads')
    # define the endTime
    endTime = time.time() + maxTime
    while True:
        try:
            # get the download percentage
            downloadPercentage = driver.execute_script(
                "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
            # check if downloadPercentage is 100 (otherwise the script will keep waiting)
            if downloadPercentage == 100:
                # exit the method once it's completed
                return downloadPercentage
        except:
            pass
        # wait for 1 second before checking the percentage next time
        time.sleep(1)
        # exit method if the download not completed with in MaxTime.
        if time.time() > endTime:
            break

def processEpisode(urls):
    # Get the episode
    browser = Chrome(executable_path="/home/stux/Downloads/chromedriver")

    for ep in urls:
        name = ep
        url = urls[ep]
        browser.get(url)

        sleep(10)

        # Make and change to the new directory
        link = browser.find_element_by_xpath("//div[@style='float:right;'][2]")
        
        print(f"{name} => {link.find_element_by_xpath('./a').get_attribute('href')}")
        sleep(5)

        link.click()
        waitUntilDownloadCompleted(browser)
        return


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
