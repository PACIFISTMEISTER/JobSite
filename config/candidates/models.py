from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Candidate(models.Model):
    """моедль соискателя"""

    class EducationChoices(models.TextChoices):
        elementary = 'elementary'
        school = 'school'
        university = 'university'

    class ExpirienceChoices(models.TextChoices):
        junior = 'junior'
        middle = 'middle'
        senior = 'senior'

    Name = models.TextField(max_length=100)
    Surname = models.TextField(max_length=100)
    Education = models.TextField(choices=EducationChoices.choices, null=True)
    Expirience = models.TextField(choices=ExpirienceChoices.choices, default='middle')
    Resume = models.FileField(upload_to='files', null=True)
    Mail = models.EmailField(null=True)
    Photo = models.ImageField(upload_to='img', null=True)
    Position = models.TextField(null=True)
    ShortInfo = models.TextField(null=True)
    Qualifications = models.TextField(null=True)

    class Meta:
        ordering = ['Name']

    def get_absolute_url(self):
        return reverse('candidateInfo', kwargs={'pk': self.id})

    def __str__(self):
        return self.Name + self.Surname
