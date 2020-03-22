#! /usr/local/bin/python3

import os
import csv
import requests
import json

def read_csv(file):

    data = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    return data


# API endpoint
API_ENDPOINT = 'http://localhost:5000/api/reports/'

# daily covid-19 reports location
daily_reports_location = '/Users/mamagdy/Code/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'

# parse all files in this directory
reports = os.listdir(daily_reports_location)

# TODO: existing reports


print(reports)
for report_name in reports:
    report_location = daily_reports_location + '/' + report_name
    data = read_csv(report_location)

    # report date
    try:
        month, day, year = report_name.split('.')[0].split('-')
        report_date = "{}-{}-{}".format(year, month, day)
    except:
        print("Cannot parse the report date {}.".format(report_name))
        continue

    body = {
        "report_date": report_date,
        "country_report": data
    }

    r = requests.post(url=API_ENDPOINT, json=body)
    print(report_name)
    print(r.json())

