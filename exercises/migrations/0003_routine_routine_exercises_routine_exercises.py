# Generated by Django 5.0.2 on 2024-11-10 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_rename_muscleexercise_muscle_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('difficulty', models.CharField(max_length=100)),
                ('estimated_duration', models.DurationField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Routine_exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(auto_created=True)),
                ('n_sets', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('repeats', models.IntegerField()),
                ('rest', models.DecimalField(decimal_places=2, max_digits=5)),
                ('exercises', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.exercise')),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.routine')),
            ],
        ),
        migrations.AddField(
            model_name='routine',
            name='exercises',
            field=models.ManyToManyField(through='exercises.Routine_exercises', to='exercises.exercise'),
        ),
    ]