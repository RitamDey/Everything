# Needs the saved copy of the webpage to get the pdf names
from re import findall
from subprocess import call


regex = r"\d{2}-[\w-]*-annotated\.pdf"
url = "http://spark-university.s3.amazonaws.com/stanford-crypto/slides/"


for pdf in findall(regex, html):
    call(["wget", url+pdf])

