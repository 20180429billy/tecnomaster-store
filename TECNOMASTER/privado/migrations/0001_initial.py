# Generated by Django 4.0 on 2023-04-25 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('image', models.ImageField(null=True, upload_to='articles')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_cliente', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_producto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_usuario', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='articles')),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_usuario', models.CharField(default='', max_length=150)),
                ('descripcion_tipo_usuario', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('apellido_usuario', models.CharField(max_length=100)),
                ('correo_usuario', models.CharField(max_length=150)),
                ('alias_usuario', models.CharField(max_length=100)),
                ('clave_usuario', models.CharField(max_length=100)),
                ('id_estado_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='privado.estadousuario')),
                ('id_tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='privado.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=100)),
                ('descripcion_producto', models.CharField(max_length=100)),
                ('precio_producto', models.IntegerField()),
                ('imagen_producto', models.ImageField(null=True, upload_to='articles')),
                ('especificaciones_producto', models.CharField(max_length=100)),
                ('descuento', models.IntegerField()),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='privado.categoria')),
                ('id_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='privado.marcas')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='privado.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_producto', models.ImageField(null=True, upload_to='articles')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='privado.producto')),
            ],
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
