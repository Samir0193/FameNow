# Generated by Django 3.2.4 on 2021-07-02 08:26

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phNo',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]