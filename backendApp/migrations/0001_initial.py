# Generated by Django 4.2.6 on 2023-10-14 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('ActividadID', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.TextField()),
                ('ValorTotal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('EventoID', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=255)),
                ('Descripcion', models.TextField(blank=True, null=True)),
                ('Tipo', models.CharField(choices=[('viaje', 'Viaje'), ('hogar', 'Hogar'), ('pareja', 'Pareja'), ('comida', 'Comida'), ('otro', 'Otro')], default='otro', max_length=10)),
                ('FotoOAvatar', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('CorreoElectronico', models.CharField(max_length=255, unique=True)),
                ('NombreCompleto', models.CharField(max_length=255)),
                ('Apodo', models.CharField(max_length=255)),
                ('FotoOAvatar', models.CharField(choices=[('avatar 1', 'https://static.vecteezy.com/system/resources/previews/019/896/012/original/female-user-avatar-icon-in-flat-design-style-person-signs-illustration-png.png'), ('avatar 2', 'https://e7.pngegg.com/pngimages/799/987/png-clipart-computer-icons-avatar-icon-design-avatar-heroes-computer-wallpaper-thumbnail.png'), ('avatar 3', 'https://cdn3.iconfinder.com/data/icons/business-avatar-1/512/11_avatar-512.png'), ('avatar 4', 'https://static.vecteezy.com/system/resources/previews/019/896/008/original/male-user-avatar-icon-in-flat-design-style-person-signs-illustration-png.png'), ('avatar 5', 'https://as1.ftcdn.net/v2/jpg/01/21/93/74/1000_F_121937450_E3o8jRG3mKbMaAFprSuNOlyrLraSVVua.jpg'), ('avatar 6', 'https://banner2.cleanpng.com/20180625/req/kisspng-computer-icons-avatar-business-computer-software-user-avatar-5b3097fcae25c3.3909949015299112927133.jpg')], default='enlace1', max_length=20)),
                ('Estado', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Saldos',
            fields=[
                ('SaldoID', models.AutoField(primary_key=True, serialize=False)),
                ('TotalDeuda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TotalPago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('EventoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.eventos')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantesEvento',
            fields=[
                ('ParticipanteID', models.AutoField(primary_key=True, serialize=False)),
                ('Estado', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=10)),
                ('EventoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.eventos')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantesActividad',
            fields=[
                ('ActividadParticipanteID', models.AutoField(primary_key=True, serialize=False)),
                ('PorcentajeParticipacion', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('ValorFijo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ActividadID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.actividades')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('PagoID', models.AutoField(primary_key=True, serialize=False)),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('FechaPago', models.DateField()),
                ('AcreedorUserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acreedor_ususario', to='backendApp.usuarios')),
                ('DeudorUserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deudor_usuario', to='backendApp.usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='eventos',
            name='Creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.usuarios'),
        ),
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('ContactID', models.AutoField(primary_key=True, serialize=False)),
                ('CorreoElectronico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos_correo', to='backendApp.usuarios', to_field='CorreoElectronico')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos_usuario', to='backendApp.usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='actividades',
            name='Creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.usuarios'),
        ),
        migrations.AddField(
            model_name='actividades',
            name='EventoID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.eventos'),
        ),
    ]
