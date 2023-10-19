# Generated by Django 4.2.6 on 2023-10-19 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0002_alter_usuarios_fotooavatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='CorreoElectronico',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Password', models.CharField(max_length=128)),
                ('Creado_en', models.DateTimeField(auto_now_add=True)),
                ('UserID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backendApp.usuarios')),
            ],
        ),
    ]
