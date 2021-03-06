# Generated by Django 3.1.8 on 2021-04-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('isPermanent', models.BooleanField(default=False, null=True)),
                ('locality', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('pincode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('Alt_Phone', models.IntegerField(blank=True)),
                ('landmark', models.CharField(max_length=255)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Map_Role_User',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('Id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('User_Role', models.CharField(db_column='User_Role', max_length=10, null=True)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True, db_column='created_on', null=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, db_column='updated_on', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Facebook', models.CharField(max_length=2048)),
                ('Twitter', models.CharField(max_length=2048)),
                ('instagram', models.CharField(max_length=2048)),
                ('whatsapp', models.CharField(max_length=2048)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
