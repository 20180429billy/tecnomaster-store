# Generated by Django 4.2 on 2023-04-24 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('privado', '0003_marcas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marcas',
            old_name='logo',
            new_name='image',
        ),
    ]
