from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from sys import argv, exit
from time import sleep
from os import mkdir, chdir, path
from subprocess import call


def setup():
    global browser

    path_driver = path.expandvars("$HOME/Downloads/")

    if path.exists(path_driver + "geckodriver") and path.isfile(path_driver + "geckodriver"):
        options = Options()
        options.add_argument("headless")
        browser = WebDriver(executable_path=path_driver + "geckodriver", options=options)
        return
    elif path.exists(path_driver + "chromedriver") and path.isfile(path_driver + "chromedriver"):
        options = ChromeOptions()
        options.add_argument("headless")
        browser = Chrome(executable_path=path_driver+"chromedriver", chrome_options=options)
        return


def processEpisode(urls):
    global browser
    # Get the episode
    for ep in urls:
        url = urls[ep]
        browser.get(url)
        sleep(10)

        # Make and change to the new directory
        link = browser.find_element_by_xpath("//div[@style='float:right;'][2]/a").get_attribute("href")
        print(f"{ep} => {link}")
        call(["wget", "--header", "Cookie: cf_clearance=f9aa953290bb30f839c889f574e76269b917cc23-1575183129-0-150; __cfduid=d0bcc2d347a2dbbd9c4682e3244e591a81575183129; BB_plg=pm; _ga=GA1.2.1706468009.1575183134; _gid=GA1.2.1377284622.1575183134; dom3ic8zudi28v8lr6fgphwffqoz0j6c=0e25db01-a70b-4b58-8918-564f18ffa042%3A1%3A1; __zlcmid=vXijCIw9adLc36; oigster=B2X2kHBdIGdzAxn4kHmhXDm1WDI5XNWgWtO4WNE=; jwplayer.captionLabel=Off; bbl=4; _gat_gtag_UA_55936626_2=1", "--no-clobber", "--continue", "-q", "--show-progress", "-O", ep + ".mp4", link])


def main(url):
    global browser
    browser.get(url)

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
        print("Need a anime url")
        exit(-1)
    url = argv[1]

    setup()
    if len(argv) > 2:
        main(url, episode=argv[2])
    else:
        main(url)

    global browser
    browser.quit()
