from django import forms
from webapp.models import Message


class ContactForm(forms.ModelForm):
    name=forms.CharField(max_length=70, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your name here'}))
    email=forms.EmailField( required=False, label='', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your email'}))
    phone = forms.CharField(required=False, max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your phone'}))
    subject = forms.CharField(required=False, max_length=400,label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Subject'}))
    message=forms.CharField(required=False, label='', widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}), max_length=1000)

    class Meta:
        model = Message
        fields = ('name', 'subject')
