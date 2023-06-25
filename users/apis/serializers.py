from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "groups", "user_permissions")


class LoginSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        "no_active_account": "We couldn't find any active account for this email and password"
    }

    def validate(self, attrs):
        data = super().validate(attrs)
        token = self.get_token(self.user)
        data["access_token"] = str(token.access_token)
        data["refresh_token"] = str(token)
        data["user"] = UserSerializer(self.user, many=False).data
        return data
