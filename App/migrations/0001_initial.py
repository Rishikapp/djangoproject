# Generated by Django 2.2.5 on 2019-10-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Head', models.CharField(max_length=50)),
                ('Descr', models.CharField(max_length=100)),
                ('Date', models.DateField(auto_now_add=True, null=True)),
                ('Img', models.ImageField(upload_to='Qwerty')),
            ],
        ),
    ]
