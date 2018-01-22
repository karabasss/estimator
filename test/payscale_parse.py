try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
from bs4 import BeautifulSoup    ## need to install # pip install beautifulsoup4
import re

link = "https://www.payscale.com/research/{country}/Job=Software_Developer/Salary/{code}/{city}"

cities = [
    {'city': 'Tallinn', 'country': 'EE', 'ps_code': '75b81c34'},
    {'city': 'Kiev', 'country': 'UA', 'ps_code': '221d38a6'},
    {'city': 'New-York-NY', 'country': 'US', 'ps_code': '5dda9200'},
    {'city': 'Helsinki', 'country': 'FI', 'ps_code': '01b00af0'}
]

for city in cities:
    #print link.format(city=city['city'],country=city['country'],code=city['ps_code'])
    url = link.format(city=city['city'],country=city['country'],code=city['ps_code'])
    soup = BeautifulSoup(urlopen(url).read(), "html.parser")
    yearly_salary = soup.find("div", {"class": "narrative-text summary"}).text
    #print ("The average pay for a software developer in " + city['city'] + " = " + yearly_salary[-1].text.split()[0] + " dollars")
    sal = re.search(r'.*\s(.*\d+,\d+).*', 'A Software Developer in New York, New York earns an average salary of $86,104')
    print (sal.group(1))
    #print (yearly_salary.text)