from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from team.models import Skill, Section, Memeber
from team.apis.serializers import MemeberSerializer
from email_validator import validate_email, EmailNotValidError


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.IsAdminUser])
def get_member(request, member_id):
    try:
        member = Memeber.objects.get(pk=member_id)
    except Memeber.DoesNotExist:
        return Response(
            {"message": "Could not find member with this id"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        serializer = MemeberSerializer(member, many=False).data
        return Response({"message": serializer}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": f"an error occurred while trying to get the member {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(
    [
        "GET",
    ]
)
@permission_classes([permissions.AllowAny])
def get_members_bysection(request, section_name):
    try:
        section = Section.objects.get(pk=section_name)
    except Section.DoesNotExist:
        return Response(
            {"message": "Couldn't find a section with this name"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        members = Memeber.objects.filter(belongs_to=section)
        serializer = MemeberSerializer(members, many=True).data
        return Response({"message": serializer}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": f"an error occurred while trying to get the members"},
            status=status.HTTP_400_BAD_REQUEST,
        )
