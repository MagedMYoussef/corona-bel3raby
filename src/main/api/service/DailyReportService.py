import datetime

from src.main.api.model.DailyReport import DailyReport
from src.main.api.util.Database import batch_save, db, commit
from src.main.api.util.CountryMap import CountryMap

KEYS = ["total_confirmed", "total_deaths", "total_recovered", "total_active", "new_confirmed", "new_deaths", "new_recovered"]


def get_report(report_date):
    if (not report_date):
        report_date = get_latest_date()

    reports = db.session.query(DailyReport).filter_by(report_date=report_date).all()
    return list(map(lambda report: {**report.serialize(), **CountryMap.get(report.country, {})}, reports))


def add_report(data):

    if not data or 'country_report' not in data or 'report_date' not in data:
        return "Invalid request body. Missing 'report_date' or 'country_report' field.", 500

    # validate report_date format
    try:
        report_date = datetime.datetime.strptime(data['report_date'], '%Y-%m-%d')
    except ValueError:
        return "Incorrect report_date format, should be YYYY-MM-DD", 400

    # validate if report_date doesn't exist
    report = DailyReport.query.filter_by(report_date=data['report_date']).first()
    if report:
        return "A report already exist with the same report_date value.", 400

    # get the latest saved report
    latest_report = get_latest_report()

    reports = data['country_report']

    # group by country
    country_reports = {}
    for report in reports:
        if report["country"] not in country_reports:
            country_reports[report["country"]] = {
                "country": report['country'],
                "report_date": report_date,
                "total_confirmed": 0,
                "total_deaths": 0,
                "total_recovered": 0
            }

        try:
            total_confirmed = int(report['Confirmed'])
        except:
            total_confirmed = 0

        try:
            total_deaths = int(report['Deaths'])
        except:
            total_deaths = 0

        try:
            total_recovered = int(report['Recovered'])
        except:
            total_recovered = 0

        country_reports[report["country"]]["total_confirmed"] += total_confirmed
        country_reports[report["country"]]["total_deaths"] += total_deaths
        country_reports[report["country"]]["total_recovered"] += total_recovered

    new_data = []
    country_reports = country_reports.values()
    for country in country_reports:

        country['total_confirmed'] = int(country['total_confirmed'])
        country['total_deaths'] = int(country['total_deaths'])
        country['total_recovered'] = int(country['total_recovered'])

        # calculate the active cases
        country["total_active"] = int(country["total_confirmed"]) - int(country["total_recovered"]) - int(country["total_deaths"])

        latest_country_report = {
            "total_confirmed": 0,
            "total_deaths": 0,
            "total_recovered": 0
        }

        # get the latest country report to be used for 'new' calculations
        if latest_report:
            temp = list(filter(lambda e: e.country == country["country"], latest_report))
            if temp:
                latest_country_report["total_confirmed"] = temp[0].total_confirmed
                latest_country_report["total_deaths"] = temp[0].total_deaths
                latest_country_report["total_recovered"] = temp[0].total_recovered

        # calculate the new cases
        country["new_confirmed"] = int(country["total_confirmed"]) - int(latest_country_report["total_confirmed"])
        country["new_deaths"] = int(country["total_deaths"]) - int(latest_country_report["total_deaths"])
        country["new_recovered"] = int(country["total_recovered"]) - int(latest_country_report["total_recovered"])

        # calculate the death rate & increase rate
        if "new_confirmed" in country and "total_confirmed" in country and country["total_confirmed"] != 0:
            country["increase_rate"] = country["new_confirmed"] / country["total_confirmed"]
        else:
            country["increase_rate"] = None

        if "total_confirmed" in country and country["total_confirmed"] != 0:
            country["death_rate"] = country["total_deaths"] / country["total_confirmed"]
        else:
            country["death_rate"] = None

        new_country_report = DailyReport(
            country=country['country'],
            report_date=report_date,
            total_confirmed=country['total_confirmed'],
            total_deaths=country['total_deaths'],
            total_recovered=country['total_recovered'],
            total_active=country['total_active'],
            new_confirmed=country['new_confirmed'],
            new_deaths=country['new_deaths'],
            new_recovered=country['new_recovered'],
            death_rate=country['death_rate'],
            increase_rate=country['increase_rate'],
        )

        new_data.append(new_country_report)

    e = batch_save(db, new_data)
    if e:
        return "An error happened while adding the report {}.".format(e), 500

    return "Report has been added successfully!", 201


def get_trends():
    # get the latest reports
    latest_reports = db.session.query(DailyReport).order_by(DailyReport.report_date).all()

    if not latest_reports:
        return {}

    # init the summary
    summary = {}
    for key in KEYS:
        summary[key] = {"worldwide": {}, "egypt": {}, "africa": {}, "arab": {}}

    # fill the summary
    for report in latest_reports:

        report = report.serialize()

        for key in KEYS:
            if report["report_date"] not in summary[key]["worldwide"]:
                summary[key]["worldwide"][report["report_date"]] = 0
            summary[key]["worldwide"][report["report_date"]] += int(report[key])

        country = get_country_info(report["country"])

        if country.get("country", None) == "Egypt":
            for key in KEYS:
                if report["report_date"] not in summary[key]["egypt"]:
                    summary[key]["egypt"][report["report_date"]] = 0
                summary[key]["egypt"][report["report_date"]] += int(report[key])
        if country.get("continent", None) == "Africa":
            for key in KEYS:
                if report["report_date"] not in summary[key]["africa"]:
                    summary[key]["africa"][report["report_date"]] = 0
                summary[key]["africa"][report["report_date"]] += int(report[key])
        if country.get("arab", None):
            for key in KEYS:
                if report["report_date"] not in summary[key]["arab"]:
                    summary[key]["arab"][report["report_date"]] = 0
                summary[key]["arab"][report["report_date"]] += int(report[key])

    return summary


def get_stats():

    # get the latest reports
    latest_reports = get_latest_report()

    if not latest_reports:
        return {}

    summary = {}
    for key in KEYS:
        summary[key] = {"worldwide": 0, "egypt": 0, "africa": 0, "arab": 0}

    for report in latest_reports:

        report = report.serialize()

        for key in KEYS:
            summary[key]["worldwide"] += int(report[key])

        country = get_country_info(report["country"])

        if country.get("country", None) == "Egypt":
            for key in KEYS:
                summary[key]["egypt"] += int(report[key])
        if country.get("continent", None) == "Africa":
            for key in KEYS:
                summary[key]["africa"] += int(report[key])
        if country.get("arab", None):
            for key in KEYS:
                summary[key]["arab"] += int(report[key])

    return summary


def get_country_info(country):
    return CountryMap.get(country, {})


def get_latest_report():

    latest_date = get_latest_date()
    if not latest_date:
        return

    latest_report = DailyReport.query.filter_by(report_date=latest_date).all()
    return latest_report


def get_latest_date():
    latest = DailyReport.query.order_by(DailyReport.report_date.desc()).first()
    if not latest:
        return

    return latest.report_date
