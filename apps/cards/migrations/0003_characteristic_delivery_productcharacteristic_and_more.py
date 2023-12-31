# Generated by Django 4.2.5 on 2023-11-12 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название характеристики')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Способ доставки')),
                ('days', models.PositiveIntegerField(verbose_name='Дни доставки')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.characteristic')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='characteristics',
            field=models.ManyToManyField(through='cards.ProductCharacteristic', to='cards.characteristic', verbose_name='Характеристики'),
        ),
        migrations.AddField(
            model_name='product',
            name='delivery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cards.delivery', verbose_name='Способ доставки'),
        ),
    ]
