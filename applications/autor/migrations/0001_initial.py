# Generated by Django 3.0 on 2024-11-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('edad', models.PositiveIntegerField()),
            ],
        ),
    ]
