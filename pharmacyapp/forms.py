from django import forms
from .models import Medicine
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.forms.widgets import PasswordInput,TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class Createuserform(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')  
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        
class Loginform(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())




# class addmnedicineform(forms.ModelForm):
#     class Meta:
#         model = Medicine
#         fields = ['medicinename','expirydate','category','quantity']



# class RegistrationForm(UserCreationForm):
#     username = forms.CharField()
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password1', 'password2'] 
        
# class loginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput())
#     password = forms.CharField(widget=forms.PasswordInput())