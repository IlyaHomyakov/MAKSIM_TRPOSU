# Generated by Django 4.0 on 2021-12-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='film_poster',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]