# Generated by Django 5.1.2 on 2024-11-04 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_big_muscle', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise_Done',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_sets', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('repeats', models.IntegerField()),
                ('rest', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateTimeField()),
                ('id_exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='MuscleExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_high_involved', models.BooleanField()),
                ('exercises', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.exercise')),
                ('muscles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.muscle')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscles',
            field=models.ManyToManyField(through='exercises.MuscleExercise', to='exercises.muscle'),
        ),
    ]
