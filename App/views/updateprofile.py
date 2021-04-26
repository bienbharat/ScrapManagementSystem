from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from App.Serializers.update_profile_serializer import UpdateProfileSerializer
from userPlus.models import User
from django.forms.models import model_to_dict

def without_keys(d, ex):
    for i in ex:
        d.pop(i)
    return d
class UpdateProfile(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [JSONParser, ]

    def put(self, request, format=None):
        user = request.user
        serializer = UpdateProfileSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(id=user.id)
        if user is not None:
            user.FirstName = serializer.validated_data['FirstName']
            user.LastName = serializer.validated_data['LastName']
            user.EmailId = serializer.validated_data['EmailId']
            user.Mobile = serializer.validated_data['Mobile']
            user.DOB = serializer.validated_data['DOB']

            user.save()
        user = User.objects.get(id=user.id)
        data = model_to_dict(user)
        print(data)
        cleaned_Data = without_keys(data,['Timezone','password'])
        return Response({
            "code": 200,
            'status': True,
            'message': 'Success',
            'data': cleaned_Data
        })



