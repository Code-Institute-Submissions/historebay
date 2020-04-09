# from django import forms
# from django.contrib.auth.models import User  # Import for creation registration form.
# from django.contrib.auth.forms import UserCreationForm  # Import for creation registration form.
# from django.core.exceptions import ValidationError


# class UserContactForm(UserCreationForm):  # Registered in views.py
#     """Form to register a new user"""

#     username = forms.CharField()
#     password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

#     class Meta:  # This inner (meta)class will provide info about the form. They can be used (amongst other feats) in Django to specify fields dat will be exposed in sending an email.
#         model = User
#         fields = ('email', 'username', 'password1', 'password2')

#     def clean_email(self):  # function to check whether an email and/ or username already exists in the database.
#         email = self.cleaned_data.get('email')
#         username = self.cleaned_data.get('username')  # Not sure if .lower can be added here...
#         if User.objects.filter(email=email).exclude(username=username):
#             raise forms.ValidationError("Email address must be unique")
#         return email

#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#         if not password1 or not password2:
#             raise ValidationError("Please confirm your password")

#         if password1 != password2:
#             raise ValidationError("Password must match")

#         return password2