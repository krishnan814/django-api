from rest_framework import serializers
from .models import Person ,Color


class RegisterSerializer(serializers.Serializer):
    email=  serializers.EmailField()
    password = serializers.CharField()
    username=serializers.CharField()





class LoginSerializer(serializers.Serializer):
    email=  serializers.EmailField()
    password = serializers.CharField()
    





class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields=['color','id']

class PeopleSerializer(serializers.ModelSerializer):

    class  Meta:
        model = Person
        fields = '__all__'


    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        
        return data
    