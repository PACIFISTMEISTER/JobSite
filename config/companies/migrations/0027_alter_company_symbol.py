# Generated by Django 4.1.1 on 2022-10-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0026_alter_company_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Symbol',
            field=models.ImageField(null=True, upload_to='static/media'),
        ),
    ]
