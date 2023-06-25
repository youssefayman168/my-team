from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from users.models import User
from email_validator import validate_email, EmailNotValidError


@api_view(
    [
        "POST",
    ]
)
@permission_classes([permissions.IsAdminUser])
def create_admin(request):
    data = request.data

    username = data.get("username")
    email = data.get("email")
    phone_number = data.get("phoneNumber")
    password = data.get("password")
    picture = request.FILES.get("picture")

    if not username:
        return Response(
            {"message": "Username is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not email:
        return Response(
            {"message": "Email is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        is_email_valid = validate_email(email)
    except EmailNotValidError:
        return Response(
            {"message": "Please enter a valid email address"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not phone_number:
        return Response(
            {"message": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not password:
        return Response(
            {"message": "Password is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    if len(password) < 6 or len(password) > 16:
        return Response(
            {
                "message": "Password should be at least 6 characters long and less than 16 characters long"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not picture:
        return Response(
            {"message": "Picture is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        User.objects.create(
            username=username,
            email=email,
            phone_number=phone_number,
            picture=picture,
            password=make_password(password),
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        return Response(
            {"message": "Admin account created successfully"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"message": f"an error occurred while account creation {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
