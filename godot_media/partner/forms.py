from django import forms
from partner.models import Partners


class PartnerForm(forms.ModelForm):

    class Meta:
        model = Partners
        fields = '__all__'
        labels = {
            'name': 'Partner Name:',
            'gst': 'Partner GST (optional):',
            'phone': 'Partner Phone:',
            'email': 'Partner email:',
            'agency': 'Agency Website:'
        }

    def __init__(self, *args, **kwargs):
        super(PartnerForm, self).__init__(*args, **kwargs)
        self.fields['gst'].required = False
