# Generated by Django 4.1.1 on 2022-10-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0003_candidate_education_candidate_mail_candidate_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='Photo',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
    ]
