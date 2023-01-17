from django import forms
from .models import QRcode 


class QRcodeForm(forms.ModelForm):
    class Meta:
        model = QRcode
        
        fields = [
            'nome',
            'link',
        ]