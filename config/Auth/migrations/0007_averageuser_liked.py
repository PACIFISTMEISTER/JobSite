# Generated by Django 4.1.1 on 2022-10-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0024_alter_company_symbol'),
        ('Auth', '0006_averageuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='averageuser',
            name='Liked',
            field=models.ManyToManyField(to='companies.job'),
        ),
    ]
