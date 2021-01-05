from django import forms
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = ContactRequest
        fields = ['email', 'name', 'content']