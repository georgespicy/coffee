# Generated by Django 4.1.1 on 2022-09-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wistara', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='table_sit',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10),
        ),
    ]
