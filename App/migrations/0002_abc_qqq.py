# Generated by Django 2.2.5 on 2019-10-25 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abc',
            name='qqq',
            field=models.CharField(default='eee', max_length=100),
            preserve_default=False,
        ),
    ]
