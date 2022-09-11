from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistionForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')