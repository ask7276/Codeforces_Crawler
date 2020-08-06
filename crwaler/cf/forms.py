from django import forms


class handle(forms.Form):
    name = forms.CharField(max_length=255, required=True)


