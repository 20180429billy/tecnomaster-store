# Generated by Django 4.2 on 2023-04-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privado', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('logo', models.ImageField(null=True, upload_to='articles')),
            ],
        ),
    ]