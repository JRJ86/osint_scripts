import requests
from bs4 import BeautifulSoup

user = 'LazadaMalaysia'
url = 'https://www.facebook.com/' + user

response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
f = soup.find('div', attrs={'class': '_4-u3 _5sqi _5sqk'})
likes = f.find('span', attrs={'class': '_52id _50f5 _50f7'})  # finding span tag inside class
print(likes.text)
