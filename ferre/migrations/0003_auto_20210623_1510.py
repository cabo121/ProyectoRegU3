# Generated by Django 3.2.4 on 2021-06-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferre', '0002_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='corona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200, null=True)),
                ('descripcion', models.CharField(default='', max_length=200, null=True)),
                ('fuente', models.CharField(default='', max_length=200, null=True)),
                ('fecha', models.CharField(default='', max_length=200, null=True)),
                ('imagen', models.ImageField(null='True', upload_to='imagen')),
            ],
        ),
        migrations.CreateModel(
            name='deportes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200, null=True)),
                ('descripcion', models.CharField(default='', max_length=200, null=True)),
                ('fuente', models.CharField(default='', max_length=200, null=True)),
                ('fecha', models.CharField(default='', max_length=200, null=True)),
                ('imagen', models.ImageField(null='True', upload_to='imagen')),
            ],
        ),
        migrations.CreateModel(
            name='nacionales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200, null=True)),
                ('descripcion', models.CharField(default='', max_length=200, null=True)),
                ('fuente', models.CharField(default='', max_length=200, null=True)),
                ('fecha', models.CharField(default='', max_length=200, null=True)),
                ('imagen', models.ImageField(null='True', upload_to='imagen')),
            ],
        ),
        migrations.DeleteModel(
            name='electricas',
        ),
        migrations.DeleteModel(
            name='manuales',
        ),
        migrations.DeleteModel(
            name='neumaticas',
        ),
    ]
