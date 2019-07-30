import requests
page = requests.get('http://examplesite.com')
contents = page.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(contents, 'html.parser')
soup.find_all('a')
print(soup)
