from re import findall
import pyperclip


text = pyperclip.paste()


ph_regex = r"\+?[\d]{10}"
email_regex = r"[\w]+\@[\w]+\.com"


print(findall(ph_regex, text))
print(findall(email_regex, text))
