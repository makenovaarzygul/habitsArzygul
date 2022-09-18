from .models import Habits
from django.forms import ModelForm,TextInput,Textarea


class HabitsForm(ModelForm):
    class Meta:
        model = Habits
        fields = ["title","habit"]
        widgets = {
            "title":TextInput(attrs={
            'class':'form-control',
            'placeholder':'Введите привычку'
        }),
        "habit":Textarea(attrs={
            'class':'form-control',
            'placeholder':'Введите описание'
        }),
        }
