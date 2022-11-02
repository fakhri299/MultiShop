# Generated by Django 4.1.1 on 2022-11-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_customer_order_orderitem_shipingadress_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='new_price',
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.FloatField(null=True),
        ),
    ]