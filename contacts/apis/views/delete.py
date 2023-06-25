from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from contacts.models import Contact


@api_view(
    [
        "DELETE",
    ]
)
@permission_classes([permissions.IsAdminUser])
def trash_contact(request, contact_id):
    try:
        contact = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        return Response(
            {"message": "Contact not found"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        contact.deleted = True
        contact.save()
        return Response(
            {"message": "Contact was trashed successfully"},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response(
            {"message": f"an error occurred while trying to star the contact {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "DELETE",
    ]
)
@permission_classes([permissions.IsAdminUser])
def delete_contact(request, contact_id):
    try:
        contact = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        return Response(
            {"message": "Contact not found"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        contact.delete()
        return Response(
            {"message": "Contact was delete successfully"},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response(
            {"message": f"an error occurred while trying to star the contact {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
