# Generated by Django 4.1.1 on 2022-09-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_person_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='summary',
            field=models.TextField(default='since this is default u will have default'),
        ),
    ]
