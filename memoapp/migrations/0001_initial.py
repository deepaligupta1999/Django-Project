# Generated by Django 3.0 on 2019-12-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
