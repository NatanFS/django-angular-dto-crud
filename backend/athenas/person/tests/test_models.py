from django.test import TestCase
from person.models import Person
from model_bakery import baker
from django.core.exceptions import ValidationError


class PersonModelTestCase(TestCase):
    def setUp(self):
        self.person_male = baker.make(
            'person.Person',
            weight=80.0,
            height=1.80,
            sex=Person.Sex.MASCULINE,
        )

        self.person_female = baker.make(
            'person.Person',
            weight=60.0,
            height=1.65,
            sex=Person.Sex.FEMININE,
        )

    def test_calculate_ideal_weight_male(self):
        self.assertEqual(float(self.person_male.ideal_weight), 72.86)

    def test_calculate_ideal_weight_female(self):
        self.assertEqual(float(self.person_female.ideal_weight), 57.77)
    
    def test_invalid_cpf_field(self):
        self.person = baker.make(
            'person.Person',
            cpf='12345678a',
        )
        self.assertRaises(ValidationError, self.person.full_clean)