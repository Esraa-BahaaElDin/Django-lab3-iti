# Generated by Django 2.2.12 on 2022-01-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('bdate', models.DateField()),
                ('intack', models.CharField(max_length=20)),
                ('track', models.CharField(max_length=20)),
                ('promotion', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]
