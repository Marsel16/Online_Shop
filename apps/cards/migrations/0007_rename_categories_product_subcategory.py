# Generated by Django 4.2.5 on 2023-11-03 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_product_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='subcategory',
        ),
    ]