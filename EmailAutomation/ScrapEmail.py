import requests
from bs4 import BeautifulSoup

URL = "https://www.scribd.com/doc/36540419/HR-EMail-IDs-of-Top-500-Indian-Companies"
r = requests.get(URL)
print(r.content)

r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib


# table = soup.find('div', attrs = {'id':'all_quotes'})
table = soup.find('div', attrs = {'id':'outer_page_1'})
# table = soup.find('div', attrs = {'id':'page1'})
for row in table.findAll('div', attrs = {'id':'page1'}):
    quote = {}
    
# print(soup.prettify())