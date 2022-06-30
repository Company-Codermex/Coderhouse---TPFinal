# Generated by Django 4.0.4 on 2022-06-28 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Accesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categoria_Accesorio',
                'verbose_name_plural': 'Categoria_Accesorios',
            },
        ),
        migrations.CreateModel(
            name='Categoria_Calzado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categoria_Calzado',
                'verbose_name_plural': 'Categoria_Calzados',
            },
        ),
        migrations.CreateModel(
            name='Categoria_Indumentaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categoria_Indumentaria',
                'verbose_name_plural': 'Categoria_Indumentarias',
            },
        ),
        migrations.CreateModel(
            name='indumentarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barra', models.CharField(max_length=40, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('talle', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('imagen', models.ImageField(null=True, upload_to='indumentaria')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nike', to='Nike.categoria_indumentaria')),
            ],
            options={
                'verbose_name': 'indumentaria',
                'verbose_name_plural': 'indumentarias',
            },
        ),
        migrations.CreateModel(
            name='calzados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barra', models.CharField(max_length=40, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('talle', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('imagen', models.ImageField(null=True, upload_to='calzado')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nike', to='Nike.categoria_calzado')),
            ],
            options={
                'verbose_name': 'calzado',
                'verbose_name_plural': 'calzados',
            },
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='accesorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barra', models.CharField(max_length=40, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('color', models.CharField(max_length=40)),
                ('imagen', models.ImageField(null=True, upload_to='accesorio')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nike', to='Nike.categoria_accesorio')),
            ],
            options={
                'verbose_name': 'accesorio',
                'verbose_name_plural': 'accesorios',
            },
        ),
    ]
