# Generated by Django 4.1.1 on 2022-10-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0017_job_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Exp',
            field=models.TextField(choices=[('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], default='Junior'),
        ),
    ]
