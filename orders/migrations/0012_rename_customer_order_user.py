# Generated by Django 4.2 on 2024-03-08 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_rename_order_id_orderitem_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='user',
        ),
    ]