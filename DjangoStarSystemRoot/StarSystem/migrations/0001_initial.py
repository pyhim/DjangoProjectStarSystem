# Generated by Django 3.2.5 on 2021-07-25 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galaxy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('size_x', models.PositiveIntegerField(default=None)),
                ('size_y', models.PositiveIntegerField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Galaxies',
            },
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('diameter', models.PositiveIntegerField(default=None)),
                ('color', models.CharField(default=None, max_length=100)),
                ('live', models.BooleanField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Planets',
            },
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('diameter', models.PositiveIntegerField(default=None)),
                ('color', models.CharField(default=None, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Stars',
            },
        ),
        migrations.CreateModel(
            name='StarSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('position_x', models.PositiveIntegerField(default=None)),
                ('position_y', models.PositiveIntegerField(default=None)),
                ('galaxy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='starsystems', to='StarSystem.galaxy')),
                ('planet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='starsystems', to='StarSystem.planet')),
                ('star', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='starsystems', to='StarSystem.star')),
            ],
            options={
                'verbose_name_plural': 'StarSystems',
            },
        ),
        migrations.AddField(
            model_name='star',
            name='star_system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stars', to='StarSystem.starsystem'),
        ),
        migrations.AddField(
            model_name='planet',
            name='star_system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planets', to='StarSystem.starsystem'),
        ),
        migrations.AddField(
            model_name='galaxy',
            name='star_system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galaxies', to='StarSystem.starsystem'),
        ),
    ]
