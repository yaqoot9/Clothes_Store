# Generated by Django 4.1.1 on 2022-10-01 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_sale_rating_favlist_creditcard'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sale',
            new_name='SoldItem',
        ),
    ]
