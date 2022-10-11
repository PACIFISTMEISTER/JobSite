from django import forms
from django.core.exceptions import ValidationError


class Login(forms.Form):
    """форма для регистрации"""
    login = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, max_length=20)


class SignUser(forms.Form):
    """форма для логина"""
    name = forms.CharField(required=True, max_length=20)
    surname = forms.CharField(required=True, max_length=20)
    login = forms.CharField(required=True, max_length=20)
    email = forms.CharField(required=True, max_length=20)
    password1 = forms.CharField(required=True, max_length=20)
    password2 = forms.CharField(required=True, max_length=20)


class CompUser(forms.Form):
    """форма для регистрации hr"""
    name = forms.CharField(required=True, max_length=20)
    surname = forms.CharField(required=True, max_length=20)
    login = forms.CharField(required=True, max_length=20)
    email = forms.CharField(required=True, max_length=20)
    password1 = forms.CharField(required=True, max_length=20)
    password2 = forms.CharField(required=True, max_length=20)
    CNN = forms.CharField(required=True, max_length=20)
    info = forms.CharField(required=True, max_length=30)
    companyname = forms.CharField(required=True, max_length=30)
    img = forms.ImageField()


class AddResume(forms.Form):
    """форма для добалвения резюме"""
    Name = forms.CharField(required=True)  #
    Surname = forms.CharField(required=True)  #
    Education = forms.CharField(required=True)  #
    Expirience = forms.CharField(required=True)  #
    Resume = forms.FileField(required=True)  #
    Mail = forms.EmailField(required=True)  #
    Photo = forms.ImageField(required=True)  #
    Position = forms.CharField(required=True)  #
    ShortInfo = forms.CharField(required=True)  #
    Qualification = forms.CharField(required=True)  #


class UpdateResume(forms.Form):
    """форма для обновления резюме"""
    Name = forms.CharField(required=True)  #
    Surname = forms.CharField(required=True)  #
    Education = forms.CharField(required=True)  #
    Expirience = forms.CharField(required=True)  #
    Resume = forms.FileField(required=False)  #
    Mail = forms.EmailField(required=True)  #
    Photo = forms.ImageField(required=False)  #
    Position = forms.CharField(required=True)  #
    ShortInfo = forms.CharField(required=True)  #
    Qualification = forms.CharField(required=True)  #


class AddJob(forms.Form):
    """форма для добавления работы от компании"""
    Name = forms.CharField(required=True)
    Position = forms.CharField(required=True)
    Description = forms.CharField(required=True)
    Responsibilities = forms.CharField(required=True)
    Qualifications = forms.CharField(required=True)
    Benefits = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Min = forms.IntegerField(required=True)
    Max = forms.IntegerField(required=True)
    Location = forms.CharField(required=True)
    Category = forms.CharField(required=True)
    Experience = forms.CharField(required=True)
    Type = forms.CharField(required=True)

    def clean(self):
        """доб валидация для показателя мин зарплаты,
         он не должен быть отрицательным, а так же больше макс зарплаты"""
        max=self.cleaned_data.get('Max')

        if self.cleaned_data['Min']<0 or self.cleaned_data['Min']>max:
            raise ValidationError("min is smaller then max or min<0")

        return self.cleaned_data


