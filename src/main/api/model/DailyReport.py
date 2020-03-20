from ..util.Database import db


class DailyReport(db.Model):
    """ User Model for storing covid-19 daily reports """
    __tablename__ = "daily_reports"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    report_date = db.Column(db.Date())
    confirmed = db.Column(db.Integer())
    deaths = db.Column(db.Integer())
    recovered = db.Column(db.Integer())

    def serialize(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
