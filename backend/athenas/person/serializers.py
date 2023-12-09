from rest_framework import serializers
from person.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'birth_date', 'cpf', 'sex',  'height', 'weight']