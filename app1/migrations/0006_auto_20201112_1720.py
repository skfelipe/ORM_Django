# Generated by Django 3.1.2 on 2020-11-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20201112_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='NombreColumna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(db_column='columna1', max_length=40)),
                ('columna2', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'TablaCursoORMDjango',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='viewcat',
            table='categoria_vies',
        ),
    ]
