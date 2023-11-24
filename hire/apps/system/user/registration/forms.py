from apps.admin.custom_user.models                  import CustomUser
from django.contrib.auth.forms                      import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model  = CustomUser
        fields = ('username', 'password1', 'password2')
