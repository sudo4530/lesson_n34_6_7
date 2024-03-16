# Generated by Django 5.0.3 on 2024-03-16 14:19

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
                ('price', models.FloatField(default=1)),
                ('image', models.ImageField(upload_to='library/author/')),
                ('count', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('student', 'S'), ('teacher', 'T')], default='S', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BookRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('took_on', models.DateField()),
                ('returned_on', models.DateField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.customers')),
            ],
        ),
    ]
