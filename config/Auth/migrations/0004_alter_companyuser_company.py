# Generated by Django 4.1.1 on 2022-10-03 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0020_company_cnn_company_someinfo'),
        ('Auth', '0003_alter_companyuser_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyuser',
            name='company',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company'),
        ),
    ]
