from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from contacts.models import Contact
from email_validator import validate_email, EmailNotValidError


@api_view(
    [
        "POST",
    ]
)
@permission_classes([permissions.AllowAny])
def create_contact(request):
    data = request.data

    if not data:
        return Response(
            {"message": "No data to send a contact message"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or name == "":
        return Response(
            {"message": "Please enter your name"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not email or email == "":
        return Response(
            {"message": "Please enter your email"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        is_email_valid = validate_email(email)
    except EmailNotValidError:
        return Response(
            {"message": "The email address is not valid"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not message or message == "":
        return Response(
            {"message": "Please enter a contact message"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        Contact.objects.create(name=name, email=email, message=message)
        return Response(
            {
                "message": "We've received your contact message, thank you for contating us!"
            },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response(
            {
                "message": f"An error occurred while trying to send your contact message {e}"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
