from django import forms
from .models import StudentDats
GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Famale')
)

class StudentForm(forms.Form):
    full_name = forms.CharField(max_length=200, label='Name', widget=forms.TextInput(attrs={'class': 'input_class'}))
    email = forms.EmailField(max_length=100, label='email address')
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        help_text='Enter your correct date of birth (YYYY-MM-DD)'
    )
    address =  forms.CharField(widget=forms.TextInput, max_length=500)
    gender =  forms.ChoiceField(choices=GENDER_CHOICE)


class StudentForm2(forms.ModelForm):
    class Meta:
        model = StudentDats
        fields = ['names', 'email', 'birth_date', 'address', 'gender']
        widgets = {
            'names': forms.TextInput(attrs={'class': 'input_class', 'placeholder': 'Your name'}),
            'email': forms.TextInput(attrs={'class': 'input_class', 'placeholder': 'email'}),
            'birth_date': forms.TextInput(attrs={'class': 'input_class', 'placeholder': 'birth_date'}),
        }

        