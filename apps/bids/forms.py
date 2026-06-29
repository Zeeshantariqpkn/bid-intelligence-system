from django import forms
from .models import Bid

class BidUploadForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['contractor_name', 'uploaded_file']
        widgets = {
            'contractor_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contractor name'
            }),
            'uploaded_file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf'
            })
        }
    
    def clean_uploaded_file(self):
        file = self.cleaned_data.get('uploaded_file')
        if file:
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError('Only PDF files are allowed.')
            if file.size > 10 * 1024 * 1024:
                raise forms.ValidationError('File size must be under 10MB.')
        return file