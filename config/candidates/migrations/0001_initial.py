# Generated by Django 4.1.1 on 2022-10-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=100)),
                ('Surname', models.TextField(max_length=100)),
                ('Education', models.TextField(choices=[('elementary', 'Elementary'), ('school', 'School'), ('university', 'University')], null=True)),
                ('Resume', models.FileField(null=True, upload_to='files')),
                ('Mail', models.EmailField(max_length=254, null=True)),
                ('Photo', models.ImageField(null=True, upload_to='img')),
                ('Position', models.TextField(null=True)),
                ('ShortInfo', models.TextField(null=True)),
                ('Qualifications', models.TextField(null=True)),
            ],
        ),
    ]