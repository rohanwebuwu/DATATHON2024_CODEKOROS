import requests
from bs4 import BeautifulSoup
url = "https://www.transfermarkt.co.uk/fc-chelsea/startseite/verein/631/saison_id/2023"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())  