from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Order


class OrderForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'appearance-none  relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-lg focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'placeholder': 'Полное имя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900  focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'placeholder': 'Email адрес'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900  focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'placeholder': 'Email адрес'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'appearance-none  relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-lg focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'placeholder': 'Телефон'}))

    class Meta:
        fields = ['fullname', 'email', 'phone', 'address']
        model = Order


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':
     'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-lg focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':
     'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-lg focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
