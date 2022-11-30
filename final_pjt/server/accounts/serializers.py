from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model


from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'id', 'new_user', 'nickname')




class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=100)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname','')
        return data
    pass
