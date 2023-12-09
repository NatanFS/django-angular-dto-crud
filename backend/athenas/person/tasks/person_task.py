from person.models import Person
from person.dtos.person_dto import PersonDTO
from person.serializers import PersonSerializer
from person.filters import PersonFilter

class PersonTask:

    @staticmethod
    def list(params=None):
        filterset = PersonFilter(params, queryset=Person.objects.all())
        return filterset.qs

    @staticmethod
    def create(person_dto):
        person = PersonDTO.dto_to_model(person_dto)
        person.save()
        return person
    
    @staticmethod
    def update(person_dto):
        person = PersonTask.get_by_id(person_dto.id)
        serializer = PersonSerializer(instance=person, data=person_dto.to_dict(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return person

    @staticmethod
    def get_by_id(person_id):
        return Person.objects.get(id=person_id)

    @staticmethod
    def delete(person_id):
        person = Person.objects.get(id=person_id)
        person.delete()
    
    @staticmethod
    def get_ideal_weight(person_id):
        person = PersonTask.get_by_id(person_id)
        return person.ideal_weight

