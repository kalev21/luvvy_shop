from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, TextInput, EmailInput, Textarea, CharField, PasswordInput, EmailField

from .models import FeedBackModel, UserDressModel
from django.contrib.auth.models import User


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBackModel
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя:',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите e-mail:',
            }),
            'subject': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема:',
            }),
            'message': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше сообщение:',
            }),
        }


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
            }))
    email = EmailField(label='Email', widget=EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите e-mail',
            }))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль',
            }))
    password2 = CharField(label='Подтверждение пароля', widget=PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Подтверждение пароль',
            }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = UserDressModel
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин',
                         widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
    password = CharField(label='Пароль',
                         widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = UserDressModel
        fields = ['username', 'password']
