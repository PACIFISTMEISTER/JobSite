# Generated by Django 4.1.1 on 2022-10-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_remove_candidate_education_remove_candidate_mail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='Education',
            field=models.TextField(choices=[('elementary', 'Elementary'), ('school', 'School'), ('university', 'University')], null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='Mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='Resume',
            field=models.FileField(null=True, upload_to='static/files'),
        ),
    ]