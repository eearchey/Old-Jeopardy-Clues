# Generated by Django 3.0.5 on 2020-04-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20200429_0440'),
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Episode', models.TextField()),
                ('Airdate', models.TextField()),
                ('Round', models.TextField()),
                ('Category', models.TextField()),
                ('Worth', models.TextField()),
                ('Clue', models.TextField()),
                ('Answer', models.TextField()),
            ],
        ),
    ]
