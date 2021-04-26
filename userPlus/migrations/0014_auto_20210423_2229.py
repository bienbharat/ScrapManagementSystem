# Generated by Django 3.1.8 on 2021-04-23 22:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userPlus', '0013_auto_20210423_0619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='IsEmailVerified',
            new_name='IsVerified',
        ),
        migrations.RemoveField(
            model_name='user',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='user',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Terms',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Timezone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='UserKey',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], db_column='gender', default='Male', max_length=100, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='Name',
            field=models.CharField(blank=True, db_column='first_name', max_length=30, verbose_name='FirstName'),
        ),
        migrations.AddField(
            model_name='user',
            name='Photo',
            field=models.ImageField(blank=True, db_column='photo', upload_to='', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='company',
            name='CompanyKey',
            field=models.CharField(db_column='company_key', db_index=True, default='5df68b1c4f', editable=False, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='EmailId',
            field=models.EmailField(db_column='email_id', max_length=254, unique=True, verbose_name='EmailId'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Mobile',
            field=models.CharField(blank=True, db_column='mobile', max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(db_column='is_superuser', default=False, verbose_name='IsSuperuser'),
        ),
    ]