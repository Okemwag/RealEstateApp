from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        error_class = 'error'
        
        
class CustomUserChangeForm(UserChangeForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        error_class = 'error'