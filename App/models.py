from django.db import models
from timezone_field import TimeZoneField
from userPlus.models import User


class Role(models.Model):
    Id = models.AutoField(primary_key=True, db_column="id")
    User_Role = models.CharField(max_length=10,null=True,db_column="User_Role")
    CreatedOn = models.DateTimeField(auto_now_add=True, null=True, db_column="created_on")
    UpdatedOn = models.DateTimeField(auto_now=True, null=True, db_column="updated_on")

    def __str__(self):
        return self.User_Role


class Map_Role_User(models.Model):
    Id = models.AutoField(primary_key=True )
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    CreatedOn = models.DateTimeField(auto_now_add=True, null=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.User.username


class Address(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    isPermanent = models.BooleanField(null=True, default=False)
    locality = models.CharField(null=False, max_length=255)
    address = models.CharField(null=False, max_length=255)
    city = models.CharField(null=False, max_length=255)
    state = models.CharField(null=False, max_length=255)
    country = models.CharField(null=False, max_length=255)
    pincode = models.IntegerField(null=False)
    phone = models.IntegerField(null=False)
    Alt_Phone = models.IntegerField(null=False, blank=True)
    landmark = models.CharField(max_length=255, null=False)
    CreatedOn = models.DateTimeField(auto_now_add=True, null=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.User.username

class Social(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Facebook = models.CharField(max_length=2048,null=False)
    Twitter = models.CharField(max_length=2048,null=False)
    instagram = models.CharField(max_length=2048,null=False)
    whatsapp = models.CharField(max_length=2048,null=False)
    CreatedOn = models.DateTimeField(auto_now_add=True, null=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.User.username








