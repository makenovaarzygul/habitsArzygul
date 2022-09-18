from sre_constants import MAX_UNTIL
from unittest.util import _MAX_LENGTH
from django.db import models

class Habits(models.Model):
    title = models.CharField('Название',max_length=50)
    habit = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ПРИВЫЧКA'
        verbose_name_plural ='ПРИВЫЧКИ'