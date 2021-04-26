from rest_framework import serializers, status
from userPlus.models import User
from rest_framework.views import Response
from django.contrib.auth import authenticate


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            if User.objects.filter(username=username).exists():
                user = authenticate(request=self.context.get('request'),
                                    username=username, password=password)

            else:
                msg = 'Phone number is not registered.'
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'code': 404,
                    'status': False,
                    'msg': 'Enter Correct Password',

                }
                raise serializers.ValidationError(msg)

        else:

            msg = {
                'code': 404,
                'status': False,
                'msg': 'Enter Correct details',

            }

            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs