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
def get_all_contacts(request):
    """
    Gets all contacts randomly
    """
    try:
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": f"Could not retrieve contact messages due to an error {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_contact(request, contact_id):
    try:
        contact = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        return Response(
            {"message": "Contact does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        serializer = ContactSerializer(contact, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": f"Could not fetch the contact details due to an error {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
