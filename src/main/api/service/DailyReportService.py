from src.main.api.model.DailyReport import DailyReport
from src.main.api.util.Database import batch_save

from src.main.api.util.Database import db
import datetime


def get_all_reports():
    reports = db.session.query(DailyReport).all()
    return list(map(lambda report: report.serialize(), reports))


def get_report(report_date):
    print(report_date)
    reports = db.session.query(DailyReport).filter_by(report_date=report_date).all()
    return list(map(lambda report: report.serialize(), reports))


def add_report(data):

    if not data or 'country_report' not in data or 'report_date' not in data:
        return "Invalid request body. Missing 'report_date' or 'country_report' field.", 500

    # validate report_date
    try:
        datetime.datetime.strptime(data['report_date'], '%Y-%m-%d')
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
            report_date=datetime.datetime.strptime(data['report_date'], '%Y-%m-%d'),
            confirmed=country['Confirmed'],
            deaths=country['Deaths'],
            recovered=country['Recovered']
        )
        new_reports.append(new_report)

    e = batch_save(db, new_reports)
    if e:
        return "An error happened while adding the report {}.".format(e), 500

    return "Report has been added successfully!", 201


def get_trends():
    pass
