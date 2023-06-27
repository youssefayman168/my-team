from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from users.apis.serializers import LoginSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            access = serializer.validated_data.get("access", None)

            refresh = serializer.validated_data.get("refresh", None)

            user = serializer.validated_data.get("user", None)
            print("serializer", serializer)

            if access is not None:
                return Response(
                    {
                        "data": user,
                        "access": access,
                        "refresh": refresh,
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception:
            return Response(
                {"message": "Something went wrong. Please try again"},
                status=status.HTTP_400_BAD_REQUEST,
            )
