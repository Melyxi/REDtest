from django.contrib.auth.forms import (AuthenticationForm,
                                       UserCreationForm,
                                       forms,
                                       UserChangeForm)
#from django.contrib.auth.models import User
from authapp.models import User

class UserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class EditFormUser(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

class EditFormAdmin(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

class EditFormDev(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'role', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_superuser':
                field.widget.attrs['class'] = ''
                field.help_text = ''
            else:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
                if field_name == 'password':
                    field.widget = forms.HiddenInput()