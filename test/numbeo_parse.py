from urllib2 import urlopen
from bs4 import BeautifulSoup    ## need to install # pip install beautifulsoup4

link="https://www.numbeo.com/cost-of-living/city-estimator/in/{city}?displayCurrency=EUR" \
"&members=4&restaurants_percentage=10.0&inexpensive_restaurants_percentage=50.0" \
"&drinking_coffee_outside=100.0&going_out_monthly=4.2&smoking_packs_per_day=0.0" \
"&alcoholic_drinks=25.0&type_of_food=0&driving_car=0.0&taxi_consumption=0.0" \
"&paying_for_public_transport=Monthly%2C+All+Members&sport_memberships=100.0" \
"&vacation=0.0&clothing_and_shoes=50.0&rent=26&displayCurrency=EUR&members=4" \
"&restaurants_percentage=10.0&inexpensive_restaurants_percentage=50.0" \
"&drinking_coffee_outside=100.0&going_out_monthly=4.2&smoking_packs_per_day=0.0" \
"&alcoholic_drinks=25.0&type_of_food=0&driving_car=0.0&taxi_consumption=0.0" \
"&paying_for_public_transport=Monthly%2C+All+Members&sport_memberships=100.0" \
"&vacation=0.0&clothing_and_shoes=50.0&rent=26"

cities = [ 'Tallinn', 'Kiev', 'New-York', 'Helsinki' ]

for city in cities:
    url = link.format(city=city)
    soup = BeautifulSoup(urlopen(url).read(), "html.parser")
    monthly_spending = soup.find_all("th", {"class": "th_no_highlight_a_right"})
    print "Monthly spending in " + city + " = " + monthly_spending[-1].text.split()[0] + " euro."


