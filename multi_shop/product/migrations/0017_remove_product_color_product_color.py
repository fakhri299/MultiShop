# Generated by Django 4.1.2 on 2022-11-05 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_category_color_size_product_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='product.color'),
        ),
    ]
