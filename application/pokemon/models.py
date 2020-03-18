from application import db

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.Text, nullable=False)
    generation = db.Column(db.Integer, nullable=False)
    released = db.Column(db.Boolean, nullable=False)

    def __init__(self, id, name, generation, released = False):
        self.id = id
        self.name = name
        self.generation = generation
        self.released = released

