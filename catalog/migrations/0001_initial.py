# Generated by Django 4.2.19 on 2025-03-07 10:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('summary', models.TextField(help_text='ingrese una breve descripcion del libro', max_length=1000, verbose_name='sinopsis')),
                ('isbn', models.CharField(help_text="13 Caracteres <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>", max_length=13, verbose_name='ISBN')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese nombre el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)) ', max_length=200, verbose_name='Genero')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='id unico para cada ejemplar', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenence'), ('o', 'On Loan'), ('a', 'available'), ('r', 'Reserved')], default='m', help_text='Disponibilidad del libro', max_length=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='Libro')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='Genre',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.author', verbose_name='Autor'),
        ),
    ]
