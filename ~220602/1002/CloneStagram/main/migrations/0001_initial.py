# Generated by Django 3.2.7 on 2021-10-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='photos/%m/%d')),
            ],
        ),
    ]
