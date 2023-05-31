import cloudscraper
from bs4 import BeautifulSoup
scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
html = scraper.get("https://www.federalpay.org/paycheck-protection-program/ny/100").content
soup = BeautifulSoup(html, 'html.parser')
print(soup)
