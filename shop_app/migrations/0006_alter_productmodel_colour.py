# Generated by Django 4.1 on 2022-12-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_productmodel_specific_alter_productmodel_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='colour',
            field=models.CharField(blank=True, choices=[('Белый', 'Белый'), ('Черный', 'Черный'), ('Бежевый', 'Бежевый')], max_length=20, verbose_name='Цвет'),
        ),
    ]
