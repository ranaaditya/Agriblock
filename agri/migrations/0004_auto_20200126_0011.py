# Generated by Django 3.0.2 on 2020-01-26 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0003_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.TextField(default='Retailer'),
        ),
    ]
