try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
from bs4 import BeautifulSoup    ## need to install # pip install beautifulsoup4

link = "https://www.payscale.com/research/{country}/Job=Software_Developer/Salary/{code}/{city}"

cities = [
    {'city': 'Tallinn', 'country': 'EE', 'ps_code': '75b81c34'},
    {'city': 'New-York-NY', 'country': 'US', 'ps_code': '5dda9200'},

]

