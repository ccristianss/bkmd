from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
# OK
class Account(models.Model):
    id_account = models.AutoField(primary_key=True)
    email_account = models.CharField(unique=True, max_length=45)
    password_account = models.CharField(max_length=255)
    dateregister_account = models.DateTimeField(auto_now_add=True)
    dateupdate_account = models.DateTimeField(auto_now=True)  
    isadmin_account = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Cifrar la contraseña antes de guardar
        self.password_account = make_password(self.password_account)
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'account'


#OK
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account_id_account', unique=True)  
    name_user = models.CharField(max_length=45)
    lastname_user = models.CharField(max_length=45)
    phone_user = models.CharField(max_length=10)
    dateregister_user = models.DateTimeField(auto_now_add=True)
    dateupdate_user = models.DateTimeField(auto_now=True)
    ismander_user = models.BooleanField(default=False) 
    image_user = models.ImageField(upload_to='users', null=True)

    class Meta:
        db_table = 'user'

#OK
class Service(models.Model):
    id_service = models.AutoField(primary_key=True)
    name_service = models.CharField(max_length=45)
    detail_service = models.CharField(max_length=255)
    image_service = models.ImageField(upload_to='services', null=True)

    class Meta:
        db_table = 'service'

#OK
class Request(models.Model):
    id_request = models.AutoField(primary_key=True)
    service = models.ForeignKey('Service', models.DO_NOTHING, db_column='service_id_service') 
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id_user')
    detail_request = models.CharField(max_length=255)
    status_request = models.CharField(max_length=15, default='Pendiente', choices=(('Pendiente', 'Pendiente'), ('Proceso', 'Proceso'), ('Finalizado', 'Finalizado')))
    dateregister_request = models.DateTimeField(auto_now_add=True)
    dateupdate_request = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = 'request'

#OK
class Mander(models.Model):
    id_mander = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id_user')
    ishavecar_mander = models.BooleanField()
    ishavemoto_mander = models.BooleanField()
    isactive_mander = models.BooleanField(default=False)
    isvalidate_mander = models.BooleanField(default=False)
    dateregister_mander = models.DateTimeField(auto_now_add=True)
    dateupdate_mander = models.DateTimeField(auto_now=True) 
    address_mander = models.CharField(max_length=100)
    cc_mander = models.CharField(max_length=13)  
    image_mander = models.ImageField(upload_to='manders', null=True)

    class Meta:
        db_table = 'mander'

class RequestManager(models.Model):
    id_requestmanager = models.AutoField(primary_key=True)  
    request = models.ForeignKey('Request', models.DO_NOTHING, db_column='request_id_request')
    mander = models.ForeignKey('Mander', models.DO_NOTHING, db_column='mander_id_mander')
    status_requestmanager = models.CharField(max_length=15, choices=(('espera', 'espera'),('proceso','proceso'),('terminado','terminado')))
    detail_requestmanager = models.CharField(max_length=45)
    dateregister_requestmanager = models.DateTimeField(auto_now_add=True)
    dateupdate_requestmanager = models.DateTimeField(auto_now=True) 
    image_requestmanager = models.ImageField(upload_to='requests', null=True)

    class Meta:
        db_table = 'requestmanager'


class Document(models.Model):
    id_document = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id_user')
    url_document = models.CharField(max_length=255) 
    isdocument_vehicle = models.BooleanField()
    isverified_document = models.BooleanField(default=False)
    TYPE_CHOICES = (
        ('CC', 'CC'),
        ('SOAT', 'SOAT'), 
        ('LICENCIA', 'LICENCIA'),
        ('OPERACION', 'OPERACION'), 
        ('TECNOMECANICA', 'TECNOMECANICA'),
        ('RECIBO', 'RECIBO')
    )
    type_document = models.CharField(max_length=15, choices=TYPE_CHOICES) 
    dateregister_document = models.DateTimeField(auto_now_add=True)
    dateupdate_document = models.DateTimeField(auto_now=True)
    dateverified_document = models.DateTimeField(null=True) 

    class Meta:
        db_table = 'document'


class Vehicle(models.Model): 
    id_vehicle = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id_user') 
    brand_vehicle = models.CharField(max_length=20) 
    plate_vehicle = models.CharField(max_length=10) 
    model_vehicle = models.SmallIntegerField() 
    color_vehicle = models.CharField(max_length=45)  
    TYPE_CHOICES = (
        ('ninguno', 'ninguno'),
        ('bicicle', 'Bicicleta'), 
        ('bike', 'Moto'), 
        ('car', 'Carro')
    )  
    type_vehicle = models.CharField(max_length=15, choices=TYPE_CHOICES)
    isverified_vehicle = models.BooleanField(default=False)
    dateregister_vehicle = models.DateTimeField(auto_now_add=True)
    dateupdate_vehicle = models.DateTimeField(auto_now=True)
    dateverified_vehicle = models.DateTimeField(null=True) 
    image_vehicle = models.ImageField(upload_to='vehicles', null=True)

    class Meta:
        db_table = 'vehicle'