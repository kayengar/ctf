import requests
from bs4 import BeautifulSoup

request = requests.get("http://check.cyberpersons.com/crossSiteCheck.html")

parseHTML = BeautifulSoup(request.text, 'html.parser')

htmlForm = parseHTML.form

formName = htmlForm['name']

print "Form name: " + formName