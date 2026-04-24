from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import News


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "category", "thumbnail", "is_featured"]


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        label="Nama Lengkap",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Masukkan nama lengkap"})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"placeholder": "Masukkan email"})
    )
    phone_number = forms.CharField(
        label="Nomor Telepon",
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Masukkan nomor telepon"})
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Pilih username"})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Minimal 6 karakter"})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Konfirmasi password"})
    )

    class Meta:
        model = User
        fields = ["full_name", "email", "phone_number", "username", "password1", "password2"]