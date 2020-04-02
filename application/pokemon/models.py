from application import db
from sqlalchemy.sql import text

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = False)
    name = db.Column(db.Text, nullable = False)
    generation = db.Column(db.Integer, nullable = False)
    released = db.Column(db.Boolean, nullable = False)

    def __init__(self, id, name, generation, released = False):
        self.id = id
        self.name = name
        self.generation = generation
        self.released = released

    @staticmethod
    def amount_released():
        stmt = text("SELECT COUNT(id) FROM Pokemon"
                    " WHERE released = '1'")
        res = db.engine.execute(stmt)
        return res.first().values()[0]

class Pogodex(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), nullable = False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable = False)
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())

    def __init__(self, trainer_id, pokemon_id):
        self.trainer_id = trainer_id
        self.pokemon_id = pokemon_id

    @staticmethod
    def amount_caught(trainer_id):
        stmt = text("SELECT COUNT(id) FROM Pogodex"
                    " WHERE trainer_id = :trainer_id").params(trainer_id = trainer_id)
        res = db.engine.execute(stmt)
        return res.first().values()[0]

    @staticmethod
    def average_caught():
        stmt = text("SELECT AVG(caught) FROM "
                    " (SELECT COUNT(Pogodex.pokemon_id) caught FROM"
                    " Trainer LEFT JOIN Pogodex ON Trainer.id = Pogodex.trainer_id"
                    " GROUP BY Trainer.id)")
        res = db.engine.execute(stmt)
        return res.first().values()[0]

