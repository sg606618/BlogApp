from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account


class SignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'password1', 'password2')


class SignInForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ('username', 'password')
