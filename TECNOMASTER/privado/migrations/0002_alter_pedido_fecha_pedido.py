# Generated by Django 4.2 on 2023-04-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
