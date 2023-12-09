from person.models import Person
from person.serializers import PersonSerializer

class PersonDTO:
    def __init__(self, name, birth_date, cpf, sex, height, weight, id=None):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf
        self.sex = sex
        self.height = height
        self.weight = weight

    def to_dict(self):
        return PersonSerializer(self).data

    @staticmethod
    def dto_to_model(dto):
        serializer = PersonSerializer(data=dto.to_dict())
        serializer.is_valid(raise_exception=True)
        return serializer.create(serializer.validated_data)

    @staticmethod
    def model_to_dto(model):
        serializer = PersonSerializer(model)
        return PersonDTO(**serializer.data)