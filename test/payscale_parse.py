try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
from bs4 import BeautifulSoup    ## need to install # pip install beautifulsoup4
import re

link = "https://www.payscale.com/research/{country}/Job=Software_Developer/Salary/{code}/{city}"
salaries = []
cities = [
    {'city': 'Tallinn', 'country': 'EE', 'ps_code': '75b81c34'},
    {'city': 'Kiev', 'country': 'UA', 'ps_code': '221d38a6'},
    {'city': 'New-York-NY', 'country': 'US', 'ps_code': '5dda9200'},
    {'city': 'Helsinki', 'country': 'FI', 'ps_code': '01b00af0'}
]

for city in cities:
    url = link.format(city=city['city'],country=city['country'],code=city['ps_code'])
    soup = BeautifulSoup(urlopen(url).read(), "html.parser")
    yearly_salary = soup.find("div", {"class": "you_label"}).text.strip()
    sal = (re.search(r'(.\d+,\d+).*', yearly_salary).group(1))
    if sal[0] == '$':
        salaries.append({'city': city['city'], 'currency': 'dollar', 'salary': int(sal[1:].replace(',', ''))})
    elif sal[0] == u'\u20AC':
        salaries.append({'city': city['city'], 'currency': 'euro', 'salary': int(sal[1:].replace(',', ''))})
    else:
        print ("Strange currency! Skipping {city} ...".format(city=city['city']))

for city in salaries:
    print ("Average salary of middle software developer in {city} = {salary} "
           "{currency}s".format(city=city['city'],salary=city['salary'],currency=city['currency']))

