# Generated by Django 4.1.1 on 2022-10-04 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_item_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favlist',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='favlist',
            name='updated_at',
        ),
    ]