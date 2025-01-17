from django import forms
from nunity_users.models import CustomUser

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter password', 'required': True}),
        label="Confirm Password",
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'device', 'gender', 'date_of_birth', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required': True}),
            'device': forms.TextInput(attrs={'placeholder': 'Device', 'required': True}),
            'gender': forms.Select(
                choices=[('male', 'Male'), ('female', 'Female')],
                attrs={'style': 'border: 1px solid gray; padding: 5px; margin: 5px; border-radius: 8px'},
            ),
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'required': True, 'class': 'date-birth'}
            ),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'required': True}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        user.set_password(cleaned_data['password'])
        if commit:
            user.save()
        return user
