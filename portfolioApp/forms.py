from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model  = ContactMessage
        fields = ["name", "email", "subject", "message"]  
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control","placeholder": "Full Name","autocomplete": "name",}),
            "email": forms.EmailInput(attrs={"class": "form-control","placeholder": "Email address","autocomplete": "email",}),
            "subject": forms.TextInput(attrs={"class": "form-control","placeholder": "Project inquiry, collaboration, etc.",}),
            "message": forms.Textarea(attrs={"class": "form-control","placeholder": "Tell me about your project, timeline, and goals...","rows": 5,}),
        }
        labels = {"name": "Full Name","email": "Email","subject": "Subject","message": "Message",}