# Generated by Django 4.1.1 on 2022-09-29 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale', to='store.item')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='store.item')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FavList', to='store.item')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FavList', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('card_number', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CreditCard', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
