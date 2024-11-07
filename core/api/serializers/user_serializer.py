from rest_framework import serializers
from core.models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True)
    confirm_password = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','password','confirm_password']

    def validate(self, attrs):
        #check if the password is match
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"Error":"Password did not match"}
            )     
        return attrs
    
    def create(self, validated_data):
        user = CustomUser(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','address','contact_number']