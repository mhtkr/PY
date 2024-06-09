import requests
from bs4 import BeautifulSoup

url = input("Enter the URL - ")
response = requests.get(url)

file_name = url.split('/')[-1]

with open(file_name, 'wb') as f:
    f.write(response.content)

