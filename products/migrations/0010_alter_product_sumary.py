# Generated by Django 4.2.6 on 2023-10-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_sumary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sumary',
            field=models.TextField(blank=True),
        ),
    ]
