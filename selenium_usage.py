from selenium import webdriver
import requests as req

url = "https://www.google.com/robots.txt"
request = req.get(url)
my_req = request.text.split('\n')

for line in my_req:
    if 'Allow' in line:
        print(line)
    else:
        continue
