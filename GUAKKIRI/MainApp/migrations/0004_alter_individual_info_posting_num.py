# Generated by Django 3.2.13 on 2022-06-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_individual_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual_info',
            name='posting_num',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
