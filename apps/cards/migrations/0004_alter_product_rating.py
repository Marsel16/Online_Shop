# Generated by Django 4.2.5 on 2023-11-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_remove_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]