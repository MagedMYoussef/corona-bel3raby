#! /usr/bin/env python3

import requests

from bs4 import BeautifulSoup
from datetime import datetime


# API endpoint
API_ENDPOINT = 'http://localhost:5000/api/reports/'


# make an actual request
page = requests.get("https://www.worldometers.info/coronavirus/")

# constructing beautiful soap object to parse html
soup = BeautifulSoup(page.content, 'html.parser')

# today's reports
table = soup.find("table", {"id": "main_table_countries_today"})
date = datetime.strftime(datetime.now(), '%Y-%m-%d')

headers = []
for header in table.find_all("th"):
    header_text = header.get_text().lower()
    if 'country' in header_text:
        header_text = 'country'
    elif 'total' in header_text and 'death' in header_text:
        header_text = 'Deaths'
    elif 'total' in header_text and 'cases' in header_text:
        header_text = 'Confirmed'
    elif 'total' in header_text and 'recover' in header_text:
        header_text = 'Recovered'
    elif 'new' in header_text and 'death' in header_text:
        header_text = 'New Deaths'
    elif 'new' in header_text and 'cases' in header_text:
        header_text = 'New Confirmed'
    elif 'new' in header_text and 'recover' in header_text:
        header_text = 'New Recovered'

    headers.append(header_text)

results = []
for row in table.find_all("tr"):

    element = {}
    for i, cell in enumerate(row.find_all("td")):
        val = cell.get_text()
        try:
            val = int(val.replace(',', '').replace('+', ''))
        except:
            pass

        element[headers[i]] = val

    if element:
        results.append(element)

body = {
    "report_date": date,
    "country_report": results
}

r = requests.post(url=API_ENDPOINT, json=body)
print(r.json())
