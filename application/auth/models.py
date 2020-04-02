from application import db
from sqlalchemy.sql import text

class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text, unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)
    admin = db.Column(db.Boolean, nullable = False)
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default = db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, username, password, admin = False):
        self.username = username
        self.password = password
        self.admin = admin

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def amount():
        stmt = text("SELECT COUNT(id) FROM Trainer")
        res = db.engine.execute(stmt)
        return res.first().values()[0]
