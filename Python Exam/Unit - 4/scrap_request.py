import requests
from bs4 import BeautifulSoup

url = "https://gmex.netlify.app/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(response)


for tag in soup.find_all("link"):
    print(tag)