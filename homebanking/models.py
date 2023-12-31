# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    # Field name made lowercase.
    customer_dni = models.TextField(db_column='customer_DNI')
    dob = models.TextField(blank=True, null=True)
    branch = models.ForeignKey('Sucursal', models.DO_NOTHING)
    card = models.ForeignKey('Tarjetas', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'cliente'


class ClienteCliente(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    dob = models.CharField(max_length=100)
    branch = models.ForeignKey('SucursalSucursal', models.DO_NOTHING)
    tipo = models.ForeignKey('ClienteTipoCliente', models.DO_NOTHING)
    usuario = models.OneToOneField(
        AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cliente_cliente'


class ClienteTipoCliente(models.Model):
    cliente_tipo = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'cliente_tipo_cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.ForeignKey(
        'TipoDeCuenta', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cuenta'


class CuentaCuenta(models.Model):
    balance = models.IntegerField()
    iban = models.CharField(max_length=100)
    cliente = models.ForeignKey(ClienteCliente, models.DO_NOTHING)
    tipo = models.ForeignKey('CuentaTipoCuenta', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'cuenta_cuenta'


class CuentaTipoCuenta(models.Model):
    cuenta_tipo = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'cuenta_tipo_cuenta'


class Direcciones(models.Model):
    address = models.TextField()

    class Meta:
        managed = True
        db_table = 'direcciones'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    # Field name made lowercase.
    employee_dni = models.TextField(db_column='employee_DNI')
    branch_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'empleado'


class Marcas(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'marcas'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sucursal'


class SucursalSucursal(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sucursal_sucursal'


class Tarjetas(models.Model):
    id_card = models.AutoField(primary_key=True)
    card_number = models.TextField()  # This field type is a guess.
    # Field name made lowercase. This field type is a guess.
    cvv = models.TextField(db_column='CVV')
    grant_date = models.TextField()
    expiration_date = models.TextField()
    card_type = models.TextField()
    brand = models.ForeignKey(Marcas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tarjetas'


class TipoDeCuenta(models.Model):
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_de_cuenta'


class TiposDeCliente(models.Model):
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipos_de_cliente'
