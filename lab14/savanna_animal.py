from app import db


class SavannaAnimal(db.Model):
    __tablename__ = "animals_db"
    animal_id = db.Column('id', db.Integer, primary_key = True)
    animal_name = db.Column('name', db.String(20))
    animal_family = db.Column('family', db.String(20))
    animal_age = db.Column('age', db.Integer)
    animal_food_weight = db.Column('food_weight', db.Integer)

    def to_string(self):
        return str("animal id: " + str(self.animal_id) + "\nanimal name: " + str(self.animal_name) + "\nanimal family: " + str(self.animal_family) + "\nanimal age: " + str(self.animal_age) + "\nanimal food weight: " + str(self.animal_food_weight))