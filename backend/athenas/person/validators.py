from django.core.exceptions import ValidationError

def validate_cpf(value):
    if not value.isdigit() or len(value) != 11:
        raise ValidationError('CPF deve ser uma string númerica com 11 dígitos.')
