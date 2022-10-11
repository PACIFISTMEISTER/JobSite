# Generated by Django 4.1.1 on 2022-10-01 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_category_remove_work_requests_alter_work_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(default='unknown')),
                ('X', models.IntegerField(default=1)),
                ('Y', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='work',
            name='Location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.location'),
        ),
    ]