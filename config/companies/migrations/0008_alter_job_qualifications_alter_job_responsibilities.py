# Generated by Django 4.1.1 on 2022-10-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_alter_work_category_alter_work_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Qualifications',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='Responsibilities',
            field=models.TextField(),
        ),
    ]
