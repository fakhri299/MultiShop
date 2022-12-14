# Generated by Django 4.1.1 on 2022-10-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_productdescription_quantity_delete_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='multi_shop/static/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ManyToManyField(default='multi_shop/static/images/default_pictures', to='product.picture'),
        ),
    ]
