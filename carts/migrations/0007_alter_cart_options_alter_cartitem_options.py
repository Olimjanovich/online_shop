# Generated by Django 4.2 on 2024-03-07 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'ordering': ['id']},
        ),
    ]
