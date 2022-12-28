# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import User
# from django.forms import ModelForm
#
# class LoginForm(forms.Form):
#     varsityEmail = forms.EmailField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#
#
# class SignUpForm(UserCreationForm):
#
#     varsityEmail = forms.EmailField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control w-full -ml-10 pl-3 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500"
#             }
#         )
#     )
#     varsityId = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control w-full -ml-10 pl-3 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500"
#             }
#         )
#     )
#     linkedIn = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control w-full -ml-10 pl-3 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500"
#             }
#         )
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control w-full -ml-10 pl-3 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500"
#             }
#         )
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control w-full -ml-10 pl-3 pr-3 py-2 rounded-lg border-2 border-gray-200 outline-none focus:border-indigo-500"
#             }
#         )
#     )
#     # check = forms.CharField(
#     #     widget=forms.TextInput(
#     #         attrs={
#     #             "class": "form-control"
#     #         }
#     #     )
#     # )
#
#
#
#     class Meta:
#         model = User
#         fields = ('varsityEmail', 'varsityId', 'linkedIn', 'password1', 'password2',)
#
