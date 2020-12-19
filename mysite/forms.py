from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['Name_Surname', 'Phone_Number', 'Subject', 'Message']
