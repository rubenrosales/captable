from django import forms


class AuthRequestForm(forms.Form):
    mobile = forms.CharField(max_length=12)


class AuthResponseForm(forms.Form):
    code = forms.CharField(max_length=4)
