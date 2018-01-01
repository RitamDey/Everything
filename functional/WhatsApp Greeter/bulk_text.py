from selenium.webdriver import Firefox


def send_texts(messages):
    # Get all the chats
    chats = driver.get_elements_by_xpath("//div[@class='_2wP_Y']")

    # Iterate over the chats
    for chat in chats:
        chat.click()  # Emulate a click on each chat

        text_box = driver.find_element_by_xpath("//div[@class='pluggable-input-body copyable-text selectable-text']")  # Get the input box element

        text_box.send_keys(text)  # Send the message

        send_key = driver.find_element_by_xpath("//button[@class='compose-btn-send']")  # Get the sent key
        send_key.click()  # Emulate a click on the button


if __name__ == '__main__':
    driver = Firefox()
    driver.get("https://web.whatsapp.com")

    input("Please check if you are signed into WhatsApp web or not and hit enter")

    send_texts("Happy New Year!!")
