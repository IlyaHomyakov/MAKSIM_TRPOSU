# Generated by Django 4.0 on 2021-12-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0006_alter_show_show_date_alter_show_show_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='film_description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]