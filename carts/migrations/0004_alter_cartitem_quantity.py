# Generated by Django 4.2 on 2024-02-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_alter_cartitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.CharField(default='', max_length=50),
        ),
    ]
