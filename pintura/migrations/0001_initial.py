# Generated by Django 2.2.7 on 2019-11-08 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pintor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pintura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('anio', models.IntegerField()),
                ('actores', models.ManyToManyField(through='pintura.Actuacion', to='pintura.Pintor')),
            ],
        ),
        migrations.AddField(
            model_name='actuacion',
            name='pintor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pintura.Pintor'),
        ),
        migrations.AddField(
            model_name='actuacion',
            name='pintura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pintura.Pintura'),
        ),
    ]
