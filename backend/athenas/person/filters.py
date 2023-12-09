from django_filters import rest_framework as filters
from person.models import Person

class PersonFilter(filters.FilterSet):
    # Define your filters based on your model fields
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    birth_date = filters.DateFilter(field_name='birth_date')
    cpf = filters.CharFilter(field_name='cpf', lookup_expr='icontains')
    sex = filters.ChoiceFilter(field_name='sex', choices=Person.Sex.choices)
    height = filters.NumberFilter(field_name='height')
    weight = filters.NumberFilter(field_name='weight')

    class Meta:
        model = Person
        fields = ['name', 'birth_date', 'cpf', 'sex', 'height', 'weight']