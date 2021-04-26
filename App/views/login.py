from rest_framework import  permissions
from App.Serializers.login_Serializer import LoginUserSerializer
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView, Response



def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return({
        'refresh' : str(refresh),
        'access' : str(refresh.access_token)
    })


class LoginAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [JSONParser,]
    def post(self, request, format=None):
        print(request.__dict__)
        print(request.user)
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = get_token_for_user(user)
        content = {
            'code': 200,
            'staus': True,
            'message': 'success',
            'Data': token,
        }
        return Response(content)

