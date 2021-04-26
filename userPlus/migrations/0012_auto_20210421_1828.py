# Generated by Django 3.1.8 on 2021-04-21 12:58

import django.core.validators
from django.db import migrations, models
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userPlus', '0011_auto_20210421_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='DOB',
            field=encrypted_fields.fields.EncryptedDateField(blank=True, db_column='DOB', null=True, verbose_name='DOB'),
        ),
        migrations.AlterField(
            model_name='company',
            name='CompanyKey',
            field=models.CharField(db_column='company_key', db_index=True, default='4506eecbc5', editable=False, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserKey',
            field=models.CharField(db_column='user_key', db_index=True, default='137b7bf0ff', editable=False, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='UserKey'),
        ),
    ]