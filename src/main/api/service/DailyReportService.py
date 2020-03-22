from src.main.api.model.DailyReport import DailyReport
from src.main.api.model.LatestReport import LatestReport
from src.main.api.util.Database import batch_save

from src.main.api.util.Database import db, commit
import datetime

from src.main.api.util.CountryMap import CountryMap

def get_all_reports():
    reports = db.session.query(DailyReport).all()
    return list(map(lambda report: report.serialize(), reports))


def get_report(report_date):
    if (report_date == "latest"):
        reports = db.session.query(LatestReport).all()
    else:
        reports = db.session.query(DailyReport).filter_by(report_date=report_date).all()
    return list(map(lambda report: report.serialize(), reports))


def add_report(data):

    if not data or 'country_report' not in data or 'report_date' not in data:
        return "Invalid request body. Missing 'report_date' or 'country_report' field.", 500

    # validate report_date
    try:
        report_date = datetime.datetime.strptime(data['report_date'], '%Y-%m-%d')
    except ValueError:
        return "Incorrect report_date format, should be YYYY-MM-DD", 400

    report = DailyReport.query.filter_by(report_date=data['report_date']).first()
    if report:
        return "A report already exist with the same report_date value.", 400

    country_report = data['country_report']
    new_reports = []
    for country in country_report:
        new_report = DailyReport(
            province=country['Province/State'],
            country=country['Country/Region'],
            report_date=report_date,
            confirmed=country['Confirmed'],
            deaths=country['Deaths'],
            recovered=country['Recovered']
        )
        new_reports.append(new_report)

    e = batch_save(db, new_reports)
    if e:
        return "An error happened while adding the report {}.".format(e), 500

    # update the latest report
    # get the latest report date to be used for updating the latest report if necessary
    latest_report = db.session.query(LatestReport).first()

    if not latest_report or (latest_report and report_date.date() > latest_report.report_date):

        db.session.query(LatestReport).delete()
        e = commit(db)
        if e:
            return e

        # insert the data
        latest_reports = []
        for country in country_report:
            new_report = LatestReport(
                province=country['Province/State'],
                country=country['Country/Region'],
                report_date=report_date,
                total_confirmed=country['Confirmed'],
                total_deaths=country['Deaths'],
                total_recovered=country['Recovered'],
                active=10,
                new_confirmed=10,
                new_deaths=10,
                new_recovered=10,
                death_rate=10,
                increase_rate=10
            )
            latest_reports.append(new_report)
        e = batch_save(db, latest_reports)
        if e:
            return "An error happened while updating the latest report {}.".format(e), 500

    return "Report has been added successfully!", 201


def get_trends():
    # get the latest reports
    latest_reports = db.session.query(DailyReport).all()
    summary = {
        "confirmed": {"worldwide": {}, "egypt": {}, "africa": {}, "arab": {}},
        "deaths": {"worldwide": {}, "egypt": {}, "africa": {}, "arab": {}},
        "recovered": {"worldwide": {}, "egypt": {}, "africa": {}, "arab": {}}
    }

    # fill the summary
    keys = ["confirmed", "deaths", "recovered"]
    for report in latest_reports:

        report = report.serialize()

        for key in keys:
            summary[key]["worldwide"][report["report_date"]] = int(report[key])

        country = get_country_info(report["country"])

        if country["country"] == "Egypt":
            for key in keys:
                summary[key]["egypt"][report["report_date"]] = int(report[key])
        if country["continent"] == "Africa":
            for key in keys:
                summary[key]["africa"][report["report_date"]] = int(report[key])
        if country["arab"]:
            for key in keys:
                summary[key]["arab"][report["report_date"]] = int(report[key])

    return summary


def get_stats():

    # get the latest reports
    latest_reports = db.session.query(LatestReport).all()
    summary = {
        "total_confirmed": {"worldwide": 0, "egypt": 0, "africa": 0, "arab": 0},
        "total_deaths": {"worldwide": 0, "egypt": 0, "africa": 0, "arab": 0},
        "total_recovered": {"worldwide": 0, "egypt": 0, "africa": 0, "arab": 0},
        "new_confirmed": {"worldwide": 0, "egypt": 0, "africa": 0, "arab": 0},
        "new_deaths": {"worldwide": 0, "egypt": 0, "africa": 0, "arab": 0},
        "new_recovered": {"worldwide": 0, "egypt": 0, "africa": 0, "arab": 0}
    }

    # fill the summary
    keys = ["total_confirmed", "total_deaths", "total_recovered", "new_confirmed", "new_deaths", "new_recovered"]
    for report in latest_reports:

        report = report.serialize()

        for key in keys:
            summary[key]["worldwide"] += int(report[key])

        country = get_country_info(report["country"])

        if country["country"] == "Egypt":
            for key in keys:
                summary[key]["egypt"] += int(report[key])
        if country["continent"] == "Africa":
            for key in keys:
                summary[key]["africa"] += int(report[key])
        if country["arab"]:
            for key in keys:
                summary[key]["arab"] += int(report[key])

    return summary


def get_country_info(country):

    if country == "Cruise Ship" or country == "St. Martin" or country == "Saint Martin" or country == "Channel Islands" or country == "Holy See" or country == "Saint Barthelemy":
        country = "Others"

    if country == "Korea, South":
        country = "South Korea"
    if country == "US":
        country = "United States"
    if country == "Czechia":
        country = "Czech Republic"
    if country == "Taiwan*":
        country = "Taiwan"

    return CountryMap[country]
