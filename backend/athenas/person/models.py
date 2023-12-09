from django.db import models

# Create your models here.
class Person(models.Model):

    class Sex(models.TextChoices):
        MASCULINE = 'M', 'Masculine'
        FEMININE = 'F', 'Feminine'

    name = models.CharField(max_length=255, verbose_name='Name', null=False)
    birth_date = models.DateField(verbose_name='Birth Date', null=False)
    cpf = models.CharField(max_length=11, verbose_name='CPF', null=False)
    sex = models.CharField(max_length=1, choices=Sex.choices, verbose_name='Sex', null=False)
    height = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Height', null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Weight', null=False)

    @property
    def calculate_ideal_weight(self):
        ideal_weight = 0
        if self.sex == self.Sex.MASCULINE:
            ideal_weight = (72.7 * self.height) - 58
        elif self.sex == self.Sex.FEMININE:
            ideal_weight = (62.1 * self.height) - 44.7
        return ideal_weight