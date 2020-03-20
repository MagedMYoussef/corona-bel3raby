from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def save_and_commit(db, data):

    db.session.add(data)

    e = commit(db)
    return e


def batch_save(db, data):

    for item in data:
        db.session.add(item)

    e = commit(db)
    return e


def commit(db):

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return e

    return
