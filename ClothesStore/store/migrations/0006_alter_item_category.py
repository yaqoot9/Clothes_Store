# Generated by Django 4.1.1 on 2022-10-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_creditcard_created_at_creditcard_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('T', 'T-shirt'), ('H', 'Hoodie'), ('O', 'Outwear'), ('S', 'Skirt'), ('P', 'Pants'), ('D', 'Dress'), ('L', 'Long Sleeve'), ('SH', 'Shorts')], max_length=10),
        ),
    ]