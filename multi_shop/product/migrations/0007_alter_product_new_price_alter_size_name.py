# Generated by Django 4.1.1 on 2022-10-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_photo_delete_picture_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new_price',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]