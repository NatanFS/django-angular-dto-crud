from rest_framework.test import APITestCase
from rest_framework import status
from person.models import Person
from model_bakery import baker 
from django.urls import reverse

class PersonViewSetTests(APITestCase):

    def setUp(self):
        self.person = baker.make('person.Person', name='João')
        self.endpoint = reverse('person_urls:person-list')

    def test_create_person(self):
        data = {
            'name': 'Alice',
            'birth_date': '1995-05-15',
            'cpf': '98765432109',
            'sex': 'F',
            'height': 1.65,
            'weight': 60.0,
        }
        response = self.client.post(self.endpoint, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 2)

    def test_list_persons(self):
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_person(self):
        response = self.client.get(f'{self.endpoint}{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_person(self):
        data = {
            'name': 'João 2',
            'birth_date': '1990-01-01',
            'cpf': '12345678901',
            'sex': 'M',
            'height': 1.75,
            'weight': 70.0,
        }
        response = self.client.put(f'{self.endpoint}{self.person.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertEqual(self.person.name, 'João 2')

    def test_delete_person(self):
        response = self.client.delete(f'{self.endpoint}{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)

    def test_ideal_weight(self):
        self.person = baker.make('person.Person', name='Lucas', weight=60.0, height=1.65, sex=Person.Sex.MASCULINE)
        response = self.client.get(f'{self.endpoint}{self.person.id}/ideal-weight/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data['ideal_weight']), 61.95)