# Generated by Django 3.2.8 on 2021-11-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='upload'),
        ),
    ]