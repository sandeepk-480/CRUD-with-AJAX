from django import forms
from app.models import MyUser

class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['name', 'email', 'password']

        # Applying Bootstrap classes
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id':'nameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id':'emailid'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id':'passwordid'})
        }