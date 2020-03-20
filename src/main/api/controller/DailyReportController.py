from flask import request
from flask_restplus import Resource

from ..service.DailyReportService import get_report, get_trends, add_report, get_all_reports


class DailyReport(Resource):
    def get(self, date=None):
        """Get the daily report, by default it should get the latest date"""
        if not date:
            reports = get_all_reports()
        else:
            reports = get_report(date)
        return reports

    def post(self):
        """Add a new report data, used by the extractor to upload the data"""
        data = request.json
        msg, status = add_report(data)
        return msg, status


class TrendGraph(Resource):
    def get(self):
        """Get the daily trends over a period of time"""
        trends = get_trends()
        return trends

