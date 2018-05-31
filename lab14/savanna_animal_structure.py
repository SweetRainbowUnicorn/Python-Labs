from app import ma


class AnimalStructure(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'family', 'age', 'weight_of_food')