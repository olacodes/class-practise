from django.contrib.auth import get_user_model
from django.forms.models import ModelForm
from forum.forms.user import CustomUserCreationForm
from forum.models.user import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
