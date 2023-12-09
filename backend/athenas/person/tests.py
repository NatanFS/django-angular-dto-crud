from django.test import TestCase
from .models import Person
from model_bakery import baker

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
        self.assertEqual(self.person_male.calculate_ideal_weight, (72.7 * 1.80) - 58)

    def test_calculate_ideal_weight_female(self):
        self.assertEqual(self.person_female.calculate_ideal_weight, (62.1 * 1.65) - 44.7)
