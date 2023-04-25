# Generated by Django 4.2 on 2023-04-24 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('privado', '0005_estadoproducto_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_producto', models.ImageField(null=True, upload_to='articles')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='privado.producto')),
            ],
        ),
    ]
