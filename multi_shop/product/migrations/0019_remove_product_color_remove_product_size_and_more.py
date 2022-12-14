# Generated by Django 4.1.1 on 2022-11-05 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_remove_product_color_product_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='product.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='product.size'),
        ),
    ]
