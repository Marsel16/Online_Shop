# Generated by Django 4.2.5 on 2023-11-09 14:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_cart_cartitem_alter_product_rating_delete_basket_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Review',
        ),
    ]