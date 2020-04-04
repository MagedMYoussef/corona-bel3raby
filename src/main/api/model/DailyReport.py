from ..util.Database import db

from datetime import date

class DailyReport(db.Model):
    """ User Model for storing covid-19 daily reports """
    __tablename__ = "daily_reports"

    country = db.Column(db.String(100), primary_key=True)
    report_date = db.Column(db.Date(), primary_key=True)
    total_confirmed = db.Column(db.Integer())
    total_deaths = db.Column(db.Integer())
    total_recovered = db.Column(db.Integer())
    total_active = db.Column(db.Integer())

    new_confirmed = db.Column(db.Integer())
    new_deaths = db.Column(db.Integer())
    new_recovered = db.Column(db.Integer())
    death_rate = db.Column(db.Float())
    increase_rate = db.Column(db.Float())

    def serialize(self):
        return {c.name: getattr(self, c.name) if not isinstance(getattr(self, c.name), date) else str(getattr(self, c.name)) for c in self.__table__.columns}
