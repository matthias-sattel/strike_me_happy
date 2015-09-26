from django import forms

class PinForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
