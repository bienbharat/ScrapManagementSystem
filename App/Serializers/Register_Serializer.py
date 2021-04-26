from rest_framework import serializers
from App.models import Address
from userPlus.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("Name", "Mobile", "EmailId", "password")
        write_only_fields = ("password", )

    def create(self, validated_data):
        print(validated_data)

