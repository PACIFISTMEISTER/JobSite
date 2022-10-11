from django import forms
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    """форма поиска"""
    keyword = forms.CharField()
    location = forms.CharField()
    category = forms.CharField()
    experience = forms.CharField()
    type = forms.CharField()


class JobForm(forms.Form):
    """форма для добавления работы"""
    Name = forms.CharField()
    Description = forms.CharField()
    Responsibilities = forms.CharField()
    Qualifications = forms.CharField()
    Benefits = forms.CharField()
    Email = forms.EmailField()
    Min = forms.IntegerField()
    Max = forms.IntegerField()
    Location = forms.CharField()
    Category = forms.CharField()
    Experience = forms.CharField()
    Type = forms.CharField()

    def clean(self):
        maxx = self.cleaned_data.get('Max')

        if self.cleaned_data['Min'] < 0 or self.cleaned_data['Min'] > maxx:
            raise ValidationError("min is smaller then max or min<0")

        return self.cleaned_data
