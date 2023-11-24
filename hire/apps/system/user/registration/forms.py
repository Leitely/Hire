import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.admin.custom_user.models import CustomUser
from django.utils.translation import gettext_lazy as _


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hide help text
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))

        return password2

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')

        if password:
            if len(password) < 8:
                self.add_error('password1', _('Your password must contain at least 8 characters.'))

        return cleaned_data

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if len(password) < 8:
            raise forms.ValidationError(_('Your password must contain at least 8 characters.'))

        # Regex pattern to match the required password format
        password_pattern = r'^[\w.@+-]+$'

        if not re.match(password_pattern, password):
            raise forms.ValidationError(
                _('Your password must contain only letters, digits, and @/./+/-/_ characters.')
            )

        return password
