from rest_framework import serializers
from users.models import Users, UserNotes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotes
        fields = ('notes')

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ('username', 'password')
