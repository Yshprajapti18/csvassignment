from django import forms
from .models import csv_data
class DocumentForm(forms.ModelForm):
    class Meta:
        model = csv_data
        fields = '__all__'