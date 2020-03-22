from ..util.Database import db


class LatestReport(db.Model):
    """ User Model for storing covid-19 latest report """
    __tablename__ = "latest_report"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    report_date = db.Column(db.Date())
    total_confirmed = db.Column(db.Integer())
    total_deaths = db.Column(db.Integer())
    total_recovered = db.Column(db.Integer())
    active = db.Column(db.Integer())
    new_confirmed = db.Column(db.Integer())
    new_deaths = db.Column(db.Integer())
    new_recovered = db.Column(db.Integer())
    death_rate = db.Column(db.Float())
    increase_rate = db.Column(db.Float())

    continent = db.Column(db.String(100))
    arab = db.Column(db.Boolean())

    def serialize(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
