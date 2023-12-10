from rest_framework import serializers
from person.models import Person

class PersonSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format='%d/%m/%Y', input_formats=['%d/%m/%Y','%d-%m-%Y', '%Y-%m-%d'])

    class Meta:
        model = Person
        fields = ['id', 'name', 'birth_date', 'cpf', 'sex',  'height', 'weight']