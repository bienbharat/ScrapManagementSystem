from rest_framework import serializers

class UpdateProfileSerializer(serializers.Serializer):
    locality = serializers.CharField(allow_null=True,allow_blank=True)
    address = serializers.CharField(allow_null=True)
    city = serializers.CharField(allow_null=True)
    state = serializers.CharField(allow_null=True)
    country = serializers.CharField(allow_null=True)
    pincode = serializers.CharField(allow_null=True)
    Phone = serializers.IntegerField(allow_null=True)
    alt_Phone = serializers.IntegerField(allow_null=True)
    landmark = serializers.CharField(allow_null=True)
    EmailId = serializers.EmailField(allow_null=True)


    def validate(self, attrs):
        locality = attrs.get('locality')
        address = attrs.get('address')
        city = attrs.get('city')
        state = attrs.get('state')
        country = attrs.get('country')
        pincode = attrs.get('pincode')
        phone = attrs.get('phone')
        Alt_Phone = attrs.get('Alt_Phone')
        landmark = attrs.get('landmark')




        print("Attrs  ", attrs)
        return attrs