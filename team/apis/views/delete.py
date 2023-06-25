from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from team.models import Skill, Section, Memeber
from email_validator import validate_email, EmailNotValidError


@api_view(
    [
        "DELETE",
    ]
)
@permission_classes([permissions.IsAdminUser])
def delete_member(request, member_id):
    try:
        member = Memeber.objects.get(id=member_id)
    except Memeber.DoesNotExist:
        return Response(
            {"message": "Could not find member with this id"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        member.delete()
        return Response(
            {"message": "Successfully deleted the member"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"message": f"Could not delete the member due to an error {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
