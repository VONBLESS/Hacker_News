from django import forms
from apps.base.models import CustomUser

# from django.contrib.auth.hashers import make_password, check_password


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def register(self):
        # Implementation for user registration logic
        # Example: Create a new CustomUser instance with the provided username and password
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # hashed_password = make_password(password)
        CustomUser.objects.create_user(username=username, password=password)

    def clean(self):
        cleaned_data = super().clean()
        # Additional validation logic if needed
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data["username"]
        if CustomUser.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    class Meta:
        model = CustomUser
        fields = ["username", "password"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
