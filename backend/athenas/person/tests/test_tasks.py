from django.test import TestCase
from datetime import date
from unittest.mock import Mock
from person.models import Person
from person.dtos.person_dto import PersonDTO
from person.serializers import PersonSerializer
from person.filters import PersonFilter
from person.tasks.person_task import PersonTask
from model_bakery import baker


class PersonTaskTests(TestCase):

    def setUp(self):
        self.mock_filter = Mock(spec=PersonFilter)
        self.mock_filter.qs = Person.objects.all()
        self.mock_serializer = Mock(spec=PersonSerializer)

    def test_list(self):
        baker.make('person.Person', name='João')
        baker.make('person.Person', name='Maria')
        persons = PersonTask.list(params={'name': 'João'})
        self.assertEqual(persons.count(), 1) 

    def test_create(self):
        dto = PersonDTO(
            name='Alice',
            birth_date=date(1990, 1, 1),
            cpf='12345678901',
            sex='F',
            height=1.70,
            weight=60.0,
        )
        person = PersonTask.create(dto)
        self.assertIsInstance(person, Person)
        self.assertEqual(Person.objects.count(), 1)

    def test_update(self):
        person = baker.make('person.Person', name='João')

        dto = PersonDTO(
            id=person.id,
            name='João 2',
            birth_date=date(1995, 5, 5),
            cpf='98765432109',
            sex='M',
            height=1.75,
            weight=70.0,
        )

        updated_person = PersonTask.update(dto)
        self.assertEqual(updated_person.name, 'João 2')

    def test_get_by_id(self):
        person = baker.make('person.Person', name='João')
        person = PersonTask.get_by_id(person.id)
        self.assertIsInstance(person, Person)

    def test_delete(self):
        person = baker.make('person.Person', name='João')

        dto = PersonDTO(
            id=person.id,
            name='João 2',
            birth_date=date(1995, 5, 5),
            cpf='98765432109',
            sex='M',
            height=1.75,
            weight=70.0,
        )
        
        PersonTask.delete(dto.id)
        self.assertEqual(Person.objects.count(), 0)
