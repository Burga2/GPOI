# Generated by Django 3.2.22 on 2023-10-06 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cognome', models.CharField(max_length=50, verbose_name='Cognome')),
                ('data_di_nascita', models.DateField(verbose_name='Data di Nascita')),
            ],
            options={
                'verbose_name': 'Autore',
                'verbose_name_plural': 'Autori',
            },
        ),
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Genere',
                'verbose_name_plural': 'Generi',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=50, verbose_name='Titolo')),
                ('autore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.autore', verbose_name='Autore')),
                ('genere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.genere', verbose_name='Genere')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libri',
            },
        ),
    ]
