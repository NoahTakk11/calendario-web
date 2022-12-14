# Generated by Django 4.0.6 on 2022-08-13 18:59

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
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_evento', models.CharField(max_length=50)),
                ('fecha_inicio_evento', models.DateField()),
                ('fecha_fin_evento', models.DateField()),
                ('hora_evento', models.CharField(max_length=5)),
                ('modalidad_evento', models.CharField(max_length=50)),
                ('descripcion_evento', models.TextField()),
                ('foto', models.ImageField(null=True, upload_to='static/')),
                ('asistencias', models.ManyToManyField(blank=True, related_name='asistencias', to=settings.AUTH_USER_MODEL)),
                ('autor_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.categoria')),
            ],
        ),
    ]
