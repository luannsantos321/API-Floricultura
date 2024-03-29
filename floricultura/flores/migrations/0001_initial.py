# Generated by Django 5.0.1 on 2024-01-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Floricultura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome da flor')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor unitário')),
            ],
        ),
    ]
