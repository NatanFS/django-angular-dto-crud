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
    def create(dto):
        person = PersonDTO.dto_to_model(dto)
        person.save()
        return person
    
    @staticmethod
    def update(dto):
        person = PersonTask.get_by_id(dto.id)
        serializer = PersonSerializer(instance=person, data=dto.to_dict(), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return person

    @staticmethod
    def get_by_id(id):
        return Person.objects.get(id=id)

    @staticmethod
    def delete(dto):
        person = Person.objects.get(id=dto.id)
        person.delete()
