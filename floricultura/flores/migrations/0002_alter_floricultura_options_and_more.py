# Generated by Django 5.0.1 on 2024-01-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='floricultura',
            options={'verbose_name': 'Floricultura'},
        ),
        migrations.AlterField(
            model_name='floricultura',
            name='quantidade',
            field=models.BigIntegerField(default=0, verbose_name='Quantidade'),
        ),
    ]