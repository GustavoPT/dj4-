from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

special_characters =  ['$', '#', '@', '!', '*', '%', '^', '&']

class RegistrationForm(forms.Form):
    email = forms.EmailField(max_length=35, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Someone already exists with that email")
        if '@' not in email:
            raise ValidationError("Email must have @ to be considered a valid email")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 4:
            raise ValidationError("Password must be of length greater than 4")
        return password

    def validate_credentials(self):
        is_proper_email = self.clean_email()
        is_proper_password = self.clean_password()
        return is_proper_email and is_proper_password


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=80, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    remember = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = User.objects.filter(email=email).first()
        if user is None or not user.check_password(password):
            raise ValidationError("That username could not be found or the password/username is incorrect")
        return cleaned_data
