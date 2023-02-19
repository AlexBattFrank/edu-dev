from rest_framework import serializers
from .models import UserProfile, Room, Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='user_detail', format='html')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile


class RoomSerializer(serializers.ModelSerializer):
    members = serializers.SlugRelatedField(many=True, slug_field='username', queryset=User.objects.all())
    url = serializers.HyperlinkedIdentityField(view_name='room_detail', read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'name', 'members')


class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='message_detail', format='html')

    class Meta:
        model = Message
        fields = ('id', 'author', 'room', 'text', 'timestamp')
