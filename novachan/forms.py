from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


# Create your views here
class SubmitPostForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100, required=False)
    text = forms.CharField(label=_('Text'), max_length=1000, required=False)
    image = forms.ImageField(label=_('Image'), required=False)


class SignupForm(auth_forms.UserCreationForm):
    email = forms.EmailField(max_length=255, help_text=_('Required'))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
