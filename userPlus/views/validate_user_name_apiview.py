from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from core.logger import get_logger
from userPlus.models import User
from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication
from django.http import HttpResponseServerError

logger = get_logger(__name__)


class ValidateUserNameSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


class ValidateUserName(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [JSONParser]
    authentication_classes = (BasicAuthentication, )

    def post(self, request, format=None):
        data = request.data
        logger.debug(request.data)
        user_name = data['username']
        try:
            entity = User.objects.filter(username=user_name)

            if len(entity) == 0:
                return Response("not_taken", status=200)
            else:
                return Response('taken', status=200)
        except Exception as ex:
            logger.error(ex)
            return HttpResponseServerError("Oops! something went wrong, We are looking at this.")



