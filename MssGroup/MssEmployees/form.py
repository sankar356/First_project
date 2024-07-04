from django import forms
from django.forms import ModelForm

from .models import User, Roles, User_details, UserData


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        # widgets = {
        #     'name': User.name(
        #         attrs={'class': 'form-control input-md', 'id': '01'}),
        #     'email': User.email(
        #         attrs={'class': 'form-control input-md', 'id': '02'}),
        #     'password': User.password(
        #         attrs={'class': 'form-control input-md', 'id': '03'}),
        #     'id_role': User.id_role(
        #         attrs={'class': 'form-control input-md', 'id': '04'}),
        #     'years_of_experience': User.years_of_experience(
        #         attrs={'class': 'form-control input-md', 'id': '05'}),
        #     'employee_num': User.employee_num(
        #         attrs={'class': 'form-control input-md', 'id': '06'}),


class RolesForm(ModelForm):
    class Meta:
        model = Roles
        fields = "__all__"


class User_details_forms(ModelForm):
    class Meta:
        model = User_details
        fields = "__all__"


class UserDataForm(ModelForm):
    class Meta:
        model = UserData
        fields = "__all__"


class DataForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': "form-control form-control-xl", 'placeholder': 'Email', 'id': 'email'}, ))
    user_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control form-control-xl", 'placeholder': 'Username', 'id': 'user_name'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "form-control form-control-xl", 'placeholder': 'Password', 'id': 'password'}))
# class UserDataForm(forms.Form):
#     user_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     password = forms.CharField(min_length=8, max_length=16)
