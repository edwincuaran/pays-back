# Generated by Django 4.2.6 on 2023-10-20 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0003_alter_usuarios_correoelectronico_passwords'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactos',
            old_name='UserID',
            new_name='Contacto_de',
        ),
        migrations.RemoveField(
            model_name='contactos',
            name='CorreoElectronico',
        ),
        migrations.AddField(
            model_name='contactos',
            name='Contacto',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='contactos_correo', to='backendApp.usuarios'),
            preserve_default=False,
        ),
    ]
