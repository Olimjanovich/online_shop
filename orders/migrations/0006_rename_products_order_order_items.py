# Generated by Django 4.2 on 2024-02-25 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='order_items',
        ),
    ]
