import re
import os
from pathlib import Path
import requests.exceptions
import urllib.request
from bs4 import BeautifulSoup
from requests import get

outputName = 'output_bs4_request'
outputName = Path(outputName) # Pathify the string

if not Path.is_dir(outputName):
    Path.mkdir(outputName)
else:
    pass
os.chdir(outputName)

keyword = 'python'
base_url = f'https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}'

response = get(base_url)

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(f'HTTP ERROR -> {error}')
else:
    print(f'response -> {response}')

web_container = BeautifulSoup(response.text, 'html.parser')

outFile = 'get_result.html'
with open(outFile, mode='w') as file:
    file.write(web_container.prettify())

web_container_id = web_container.find(id='category-2')

id_getFile = 'get_id_result.html'
with open(id_getFile, mode='w') as file:
    file.write(web_container_id.prettify())

web_container_img = web_container.find('div', class_='flag-logo')

img_getFile = 'get_img_result.html'
with open(img_getFile, mode='w') as file:
    file.write(web_container_id.prettify())

print('Use select() method')
web_select = web_container.select('div.flag-logo')
print(web_select)
# Modified Version :
web_select2 = web_container.select('.flag-logo')
print(web_select2)
print()

with open('temp.html', mode='w') as file:
    for item in web_select2:
        style_tag = item.get('style')
        file.write(style_tag)

print(web_container_img.attrs)
print(type(web_container_img.attrs))  # .attrs put results tags in a dictionary
print(web_container_img.attrs['style'])
string = web_container_img.attrs['style']

print(style_tag.split('(')[1].split(')')[0])

pattern = r'url\((.*?)\)'
print('pattern : {}, string : {}'.format(pattern, string))
match = re.search(pattern, string)
print(f'match : {match.group(1)}')
URL = match.group(1)
filename = 'image.jpg'
urllib.request.urlretrieve(URL, filename) # Download image
