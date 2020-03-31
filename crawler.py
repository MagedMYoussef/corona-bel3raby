import requests
from bs4 import BeautifulSoup
import json


'''
    {'headers' : ['countries', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 
                'total_recovered', 'active_cases', 'critical', 'total_cases_1M_pop', 'deaths_1M_pop', 'reported_1st_case'}],
     'total_countries' : <num>,
     'country_1' : [<data_1>, ....., <data_11>]
     .....
     .....
     .....
     .....
     'country_n' : [<data_1>, ....., <data_11>]
'''

# start by building the json object
json_data = {}
json_data['headers'] = ['countries', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 
                        'total_recovered', 'active_cases', 'critical', 'total_cases_1M_pop', 'deaths_1M_pop', 'reported_1st_case']

json_data['total_countries'] = 0 # to keep track of the number of countries in order to easily parse it.

# make an actual request
page = requests.get("https://www.worldometers.info/coronavirus/?fbclid=IwAR1oGk8-C0edLdHL9HtjgYS_rEzdOsCVxVJ2rVwoZV1ya65HHNQ48I2THgw")

# constructing beautiful soap object to parse html
soup = BeautifulSoup(page.content, 'html.parser')

# finding the table
table = soup.find('table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

# iterate over the rows
for num, row in enumerate(rows):
    # find the colums
    cols = row.find_all('td')
    cols = [content.text.strip() for content in cols] #get the data inside the columns
    json_data['country'+str(num)] = cols
    json_data['total_countries'] += 1

print (json.dumps(json_data))