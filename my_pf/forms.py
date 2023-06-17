from django import forms
from .models import PersonalDetails, Headings, Skills, Project


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = '__all__'

class HeadingsForm(forms.ModelForm):
    class Meta:
        model = Headings
        exclude = []  # Exclude all fields by default
        widgets = {
            'big_header': forms.Textarea(attrs={'rows':3, 'cols': 70}),
            'sub_header': forms.Textarea(attrs={'rows':3, 'cols': 70}),
            'par1': forms.Textarea(attrs={'rows': 3, 'cols': 70}),
            'par2': forms.Textarea(attrs={'rows': 3, 'cols': 70}),
            'par3': forms.Textarea(attrs={'rows': 3, 'cols': 70}),
            'par4': forms.Textarea(attrs={'rows': 3, 'cols': 70}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].required = False  # Set the profile_image field as not required

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'description', 'github_url']