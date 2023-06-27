from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from contacts.models import Contact
from contacts.apis.serializers import ContactSerializer


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_latest_contacts(request):
    try:
        contacts = Contact.objects.all().order_by("-sent_at")
        serializer = ContactSerializer(contacts, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": f"an error occurred while retrieving contacts {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_seen_contacts(request):
    try:
        contacts = Contact.objects.filter(read=True)
        serializer = ContactSerializer(contacts, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": f"an error occurred while retrieving contacts {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_starred_contacts(request):
    try:
        contacts = Contact.objects.filter(starred=True)
        serializer = ContactSerializer(contacts, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": f"an error occurred while retrieving contacts {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_trashed_contacts(request):
    try:
        contacts = Contact.objects.filter(deleted=True)
        serializer = ContactSerializer(contacts, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": f"an error occurred while retrieving contacts {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
