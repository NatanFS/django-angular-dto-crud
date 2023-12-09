from person.models import Person
from person.tasks.person_task import PersonTask
from person.serializers import PersonSerializer
from person.dtos.person_dto import PersonDTO

class PersonService:

    @staticmethod
    def list(params=None):
        people = PersonTask.list(params)
        return [PersonDTO.model_to_dto(person) for person in people]

    @staticmethod
    def create(person_data):
        serializer = PersonSerializer(data=person_data)
        serializer.is_valid(raise_exception=True)
        person_dto = PersonDTO(**serializer.validated_data)
        person = PersonTask.create(person_dto)
        return PersonDTO.model_to_dto(person)

    @staticmethod
    def update(person_id, update_data):
        person_dto = PersonService.get_by_id(person_id)
        serializer = PersonSerializer(instance=person_dto, data=update_data, partial=True)
        serializer.is_valid(raise_exception=True)
        for key, value in serializer.validated_data.items():
            setattr(person_dto, key, value)
        person = PersonTask.update(person_dto)
        return PersonDTO.model_to_dto(person)

    @staticmethod
    def delete(person_id):
        person_dto = PersonService.get_by_id(person_id)
        PersonTask.delete(person_dto)
    
    @staticmethod
    def get_by_id(person_id):
        person = PersonTask.get_by_id(person_id)
        return PersonDTO.model_to_dto(person)
    