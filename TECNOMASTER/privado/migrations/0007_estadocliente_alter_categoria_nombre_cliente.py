# Generated by Django 4.0 on 2023-04-20 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('privado', '0006_alter_categoria_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_cliente', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('dui', models.IntegerField()),
                ('correo', models.CharField(max_length=150)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=250)),
                ('clave', models.CharField(max_length=150)),
                ('usuario', models.CharField(max_length=150)),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='privado.estadocliente')),
            ],
        ),
    ]
