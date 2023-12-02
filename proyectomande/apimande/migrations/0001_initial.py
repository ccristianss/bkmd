# Generated by Django 4.2.7 on 2023-12-02 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id_account', models.AutoField(primary_key=True, serialize=False)),
                ('email_account', models.CharField(max_length=45, unique=True)),
                ('password_account', models.CharField(max_length=255)),
                ('dateregister_account', models.DateTimeField(auto_now_add=True)),
                ('dateupdate_account', models.DateTimeField(auto_now=True)),
                ('isadmin_account', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'account',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mander',
            fields=[
                ('id_mander', models.AutoField(primary_key=True, serialize=False)),
                ('ishavecar_mander', models.BooleanField()),
                ('ishavemoto_mander', models.BooleanField()),
                ('isactive_mander', models.BooleanField(default=False)),
                ('isvalidate_mander', models.BooleanField(default=False)),
                ('dateregister_mander', models.DateTimeField(auto_now_add=True)),
                ('dateupdate_mander', models.DateTimeField(auto_now=True)),
                ('address_mander', models.CharField(max_length=100)),
                ('cc_mander', models.CharField(max_length=13)),
                ('image_mander', models.ImageField(null=True, upload_to='manders')),
            ],
            options={
                'db_table': 'mander',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id_request', models.AutoField(primary_key=True, serialize=False)),
                ('detail_request', models.CharField(max_length=255)),
                ('status_request', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Proceso', 'Proceso'), ('Finalizado', 'Finalizado')], default='Pendiente', max_length=15)),
                ('dateregister_request', models.DateTimeField(auto_now_add=True)),
                ('dateupdate_request', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'request',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id_service', models.AutoField(primary_key=True, serialize=False)),
                ('name_service', models.CharField(max_length=45)),
                ('detail_service', models.CharField(max_length=255)),
                ('image_service', models.ImageField(null=True, upload_to='services')),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name_user', models.CharField(max_length=45)),
                ('lastname_user', models.CharField(max_length=45)),
                ('phone_user', models.CharField(max_length=10)),
                ('dateregister_user', models.DateTimeField(auto_now_add=True)),
                ('dateupdate_user', models.DateTimeField(auto_now=True)),
                ('ismander_user', models.BooleanField(default=False)),
                ('image_user', models.ImageField(null=True, upload_to='users')),
                ('account', models.ForeignKey(db_column='account_id_account', on_delete=django.db.models.deletion.DO_NOTHING, to='apimande.account')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id_vehicle', models.AutoField(primary_key=True, serialize=False)),
                ('brand_vehicle', models.CharField(max_length=20)),
                ('plate_vehicle', models.CharField(max_length=10)),
                ('model_vehicle', models.SmallIntegerField()),
                ('color_vehicle', models.CharField(max_length=45)),
                ('type_vehicle', models.CharField(choices=[('ninguno', 'ninguno'), ('bicicle', 'Bicicleta'), ('bike', 'Moto'), ('car', 'Carro')], max_length=15)),
                ('isverified_vehicle', models.BooleanField(default=False)),
                ('dateregister_vehicle', models.DateTimeField(auto_now_add=True)),
                ('dateupdate_vehicle', models.DateTimeField(auto_now=True)),
                ('dateverified_vehicle', models.DateTimeField(null=True)),
                ('image_vehicle', models.ImageField(null=True, upload_to='vehicles')),
                ('user', models.ForeignKey(db_column='user_id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='apimande.user')),
            ],
            options={
                'db_table': 'vehicle',
            },
        ),
        migrations.CreateModel(
            name='RequestManager',
            fields=[
                ('id_requestmanager', models.AutoField(primary_key=True, serialize=False)),
                ('status_requestmanager', models.CharField(choices=[('espera', 'espera'), ('proceso', 'proceso'), ('terminado', 'terminado')], max_length=15)),
                ('detail_requestmanager', models.CharField(max_length=45)),
                ('dateregister_requestmanager', models.DateTimeField(auto_now_add=True)),
                ('dateupdate_requestmanager', models.DateTimeField(auto_now=True)),
                ('image_requestmanager', models.ImageField(null=True, upload_to='requests')),
                ('mander', models.ForeignKey(db_column='mander_id_mander', on_delete=django.db.models.deletion.DO_NOTHING, to='apimande.mander')),
                ('request', models.ForeignKey(db_column='request_id_request', on_delete=django.db.models.deletion.DO_NOTHING, to='apimande.request')),
            ],
            options={
                'db_table': 'requestmanager',
            },
        ),
        migrations.AddField(
            model_name='request',
            name='service',
            field=models.ForeignKey(db_column='service_id_service', on_delete=django.db.models.deletion.DO_NOTHING, to='apimande.service'),
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(db_column='user_id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='apimande.user'),
        ),
        migrations.AddField(
            model_name='mander',
            name='user',
            field=models.ForeignKey(db_column='user_id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='apimande.user'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id_document', models.AutoField(primary_key=True, serialize=False)),
                ('url_document', models.CharField(max_length=255)),
                ('isdocument_vehicle', models.BooleanField()),
                ('isverified_document', models.BooleanField(default=False)),
                ('type_document', models.CharField(choices=[('CC', 'CC'), ('SOAT', 'SOAT'), ('LICENCIA', 'LICENCIA'), ('OPERACION', 'OPERACION'), ('TECNOMECANICA', 'TECNOMECANICA'), ('RECIBO', 'RECIBO')], max_length=15)),
                ('dateregister_document', models.DateTimeField(auto_now_add=True)),
                ('dateupdate_document', models.DateTimeField(auto_now=True)),
                ('dateverified_document', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(db_column='user_id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='apimande.user')),
            ],
            options={
                'db_table': 'document',
            },
        ),
    ]