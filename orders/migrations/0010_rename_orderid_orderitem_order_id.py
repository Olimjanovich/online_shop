# Generated by Django 4.2 on 2024-03-08 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_rename_order_orderitem_orderid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='orderID',
            new_name='order_id',
        ),
    ]
