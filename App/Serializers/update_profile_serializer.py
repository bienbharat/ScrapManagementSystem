from rest_framework import serializers

class UpdateProfileSerializer(serializers.Serializer):
    FirstName = serializers.CharField(allow_null=True)
    LastName = serializers.CharField(allow_null=True)
    Mobile = serializers.IntegerField(allow_null=True)
    EmailId = serializers.EmailField(allow_null=True)
    DOB = serializers.DateField(allow_null=True)


    def validate(self, attrs):

        FirstName = attrs.get('FirstName')
        LastName = attrs.get('LastName')
        Mobile = attrs.get('Mobile')
        EmailId = attrs.get('EmailId')
        DOB = attrs.get('DOB')



        print("Attrs  ", attrs)
        return attrs