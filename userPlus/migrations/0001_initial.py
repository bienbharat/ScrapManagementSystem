# Generated by Django 3.2 on 2021-04-20 05:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import encrypted_fields.fields
import timezone_field.fields
import userPlus.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('Id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('Id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('CompanyKey', models.CharField(db_column='company_key', db_index=True, default='fd6c132cf0', editable=False, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('CompanyName', models.CharField(db_column='company_name', max_length=100, null=True, verbose_name='Company Name')),
                ('LegalName', models.CharField(db_column='legal_name', max_length=100, null=True, verbose_name='Legal Name')),
                ('PANCard', models.CharField(db_column='pan_card', max_length=30, null=True, verbose_name='PAN Card')),
                ('TaxID', models.CharField(db_column='tax_id', max_length=50, null=True, verbose_name='Tax ID')),
                ('Username', models.CharField(db_column='username', max_length=50, null=True, verbose_name='User Name')),
                ('Mobile', models.CharField(db_column='mobile', max_length=40, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Mobile')),
                ('AddressLine1', models.CharField(db_column='address_line_1', max_length=50, null=True, verbose_name='Address Line 1')),
                ('AddressLine2', models.CharField(db_column='address_line_2', max_length=50, null=True, verbose_name='Address Line 2')),
                ('Locality', models.CharField(db_column='locality', max_length=50, null=True, verbose_name='Locality')),
                ('City', models.CharField(db_column='city', max_length=50, null=True, verbose_name='City')),
                ('State', models.CharField(db_column='state', max_length=50, null=True, verbose_name='State')),
                ('PostalCode', models.IntegerField(db_column='postal_code', null=True, verbose_name='Postal Code')),
                ('CreatedOn', models.DateTimeField(auto_now_add=True, db_column='created_on', null=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, db_column='updated_on', null=True)),
                ('IsActive', models.BooleanField(db_column='is_active', db_index=True, default=True)),
                ('Country', models.ForeignKey(db_column='country', null=True, on_delete=django.db.models.deletion.CASCADE, to='userPlus.country')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('UserKey', models.CharField(db_column='user_key', db_index=True, default='c0495b4818', editable=False, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='UserKey')),
                ('EmailId', encrypted_fields.fields.EncryptedEmailField(db_column='email_id', max_length=254, verbose_name='EmailId')),
                ('username', models.CharField(db_column='username', max_length=30, null=True, unique=True, verbose_name='username')),
                ('FirstName', encrypted_fields.fields.EncryptedCharField(blank=True, db_column='first_name', max_length=30, verbose_name='FirstName')),
                ('LastName', encrypted_fields.fields.EncryptedCharField(blank=True, db_column='last_name', max_length=30, verbose_name='LastName')),
                ('Mobile', encrypted_fields.fields.EncryptedCharField(blank=True, db_column='mobile', max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Mobile')),
                ('Terms', models.BooleanField(db_column='terms_and_conditions', default=False, verbose_name='Terms and Conditions')),
                ('CreatedOn', models.DateTimeField(auto_now_add=True, db_column='created_on', null=True, verbose_name='CreatedOn')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, db_column='updated_on', null=True, verbose_name='UpdatedOn')),
                ('IsEmailVerified', models.BooleanField(db_column='is_emailVerified', default=False, verbose_name='IsEmailVerified')),
                ('IsActive', models.BooleanField(db_column='is_active', default=False, verbose_name='IsActive')),
                ('is_staff', models.BooleanField(db_column='is_staff', default=False, verbose_name='is_staff')),
                ('is_superuser', models.BooleanField(db_column='is_superuser', default=False, verbose_name='is_superuser')),
                ('Timezone', timezone_field.fields.TimeZoneField(db_column='timezone', default='Indian/Christmas')),
                ('LastLoginIP', models.GenericIPAddressField(blank=True, db_column='last_login_ip', null=True)),
                ('Company', models.ForeignKey(db_column='company_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Users', to='userPlus.company')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
            managers=[
                ('objects', userPlus.models.UserManager()),
            ],
        ),
    ]