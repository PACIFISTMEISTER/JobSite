# Generated by Django 4.1.1 on 2022-09-30 18:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_work_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Rating', models.IntegerField(choices=[(1, 'Awful'), (2, 'Bad'), (3, 'Better'), (4, 'Good'), (5, 'Best')])),
            ],
        ),
        migrations.AlterField(
            model_name='work',
            name='Requests',
            field=models.PositiveBigIntegerField(db_index=True),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=20)),
                ('Type', models.TextField(choices=[('part_time', 'Part Time'), ('full_time', 'Full Time')])),
                ('Description', models.TextField(max_length=500)),
                ('Responsibilities', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=50), size=None)),
                ('Qualifications', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=50), size=None)),
                ('Benefits', models.TextField(max_length=500)),
                ('Email', models.EmailField(max_length=254)),
                ('Published', models.DateField(auto_now=True)),
                ('Min_salary', models.PositiveSmallIntegerField()),
                ('Max_salary', models.PositiveSmallIntegerField()),
                ('Company', models.ManyToManyField(to='companies.company')),
                ('Work_data', models.ManyToManyField(to='companies.work')),
            ],
        ),
    ]
