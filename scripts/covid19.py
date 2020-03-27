#! /usr/local/bin/python3

import csv
import requests
import json
import glob
import os


def read_csv(file):

    data = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:

            # map the country fields
            if "Country_Region" in row:
                row["country"] = row["Country_Region"]
            elif "Country/Region" in row:
                row["country"] = row["Country/Region"]
            else:
                continue

            data.append(row)

    return data


# API endpoint
API_ENDPOINT = 'http://localhost:5000/api/reports/'

# daily covid-19 reports location
DATA_LOCATION = '/Users/mamagdy/Code/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'

# parse all files in this directory
reports = list(filter(os.path.isfile, glob.glob(DATA_LOCATION + "*")))
reports.sort(key=lambda x: os.path.getmtime(x))

print(reports)

for report_name in reports:
    data = read_csv(report_name)

    if not data:
        print("No data parsed! {}".format(report_name))
        continue

    # report date extraction
    try:
        month, day, year = report_name.split('/')[-1].split('.')[0].split('-')
        report_date = "{}-{}-{}".format(year, month, day)
    except:
        print("Cannot parse the report date {}.".format(report_name))
        continue

    body = {
        "report_date": report_date,
        "country_report": data
    }

    r = requests.post(url=API_ENDPOINT, json=body)
    print(r.json())

