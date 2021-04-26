# from rest_framework import generics, permissions,status
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
# from userPlus.models import User
# from App.Serializers.Register_Serializer import UserSerializer
#
#
# class RegisterAPI(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     parser_classes = [JSONParser,]
#     queryset = User.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#
#         print(serializer.data)
#         content = {
#             'code': 200,
#             'status': True,
#             'message': 'notVerify',
#             'Data': serializer.data,
#             }
#         return Response(content)

from rest_framework import generics
from userPlus.models import User
from App.Serializers.Register_Serializer import UserSerializer


class RegisterAPI(generics.CreateAPIView):
    """
    Create a new ModelA entry with ModelB entry
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
