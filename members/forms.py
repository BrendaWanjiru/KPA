from django import forms
from .models import Image
from .models import Member

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['MemberID', 'Fullname']

