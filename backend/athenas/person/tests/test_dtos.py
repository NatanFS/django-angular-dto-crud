from django.test import TestCase
from person.models import Person
from person.dtos.person_dto import PersonDTO
from datetime import date
from decimal import Decimal

class TestPersonDTO(TestCase):

    def test_initialization(self):
        dto = PersonDTO(
            name='João',
            birth_date=date(1990, 1, 1),
            cpf='12345678901',
            sex='M',
            height=1.75,
            weight=70.0,
            id=1,
        )
        self.assertEqual(dto.id, 1)
        self.assertEqual(dto.name, 'João')
        self.assertEqual(dto.birth_date, date(1990, 1, 1))
        self.assertEqual(dto.cpf, '12345678901')
        self.assertEqual(dto.sex, 'M')
        self.assertEqual(dto.height, 1.75)
        self.assertEqual(dto.weight, 70.0)

    def test_to_dict(self):
        dto = PersonDTO(
            name='Maria',
            birth_date=date(1995, 5, 15),
            cpf='98765432109',
            sex='F',
            height=1.65,
            weight=60.0,
        )
        dto_dict = dto.to_dict()
        self.assertIsInstance(dto_dict, dict)
        self.assertEqual(dto_dict['name'], 'Maria')
        self.assertEqual(dto_dict['birth_date'], '1995-05-15')
        self.assertEqual(dto_dict['cpf'], '98765432109')
        self.assertEqual(dto_dict['sex'], 'F')
        self.assertEqual(dto_dict['height'], '1.65')
        self.assertEqual(dto_dict['weight'], '60.00')

    def test_dto_to_model(self):
        dto = PersonDTO(
            name='Alice',
            birth_date=date(1980, 3, 10),
            cpf='12312312312',
            sex='F',
            height=1.60,
            weight=55.0,
        )
        model = PersonDTO.dto_to_model(dto)
        self.assertIsInstance(model, Person)  
        self.assertEqual(model.name, 'Alice')
        self.assertEqual(model.birth_date, date(1980, 3, 10))
        self.assertEqual(model.cpf, '12312312312')
        self.assertEqual(model.sex, 'F')
        self.assertEqual(model.height, Decimal('1.60'))
        self.assertEqual(model.weight, Decimal('55.00'))

    def test_model_to_dto(self):
        model = Person(  
            name='Marcos',
            birth_date=date(1975, 8, 20),
            cpf='45645645645',
            sex='M',
            height=1.80,
            weight=75.0,
        )
        dto = PersonDTO.model_to_dto(model)
        self.assertIsInstance(dto, PersonDTO)
        self.assertEqual(dto.name, 'Marcos')
        self.assertEqual(dto.birth_date, str(date(1975, 8, 20)))
        self.assertEqual(dto.cpf, '45645645645')
        self.assertEqual(dto.sex, 'M')
        self.assertEqual(dto.height, '1.80')
        self.assertEqual(dto.weight, '75.00')


