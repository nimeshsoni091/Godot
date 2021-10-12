from django import forms

from member.models import Members


class MemberForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = ('name', 'email', 'phone')
        labels = {
            'name': 'Member Name:',
            'email': 'Member email:',
            'phone': 'Member Phone:',
        }
