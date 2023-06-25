from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from team.models import Skill
from team.apis.serializers import SkillSerializer


@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])
def get_all_skills(request):
    try:
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"message": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {
                "message": f"an error occurred while retrieving all skill information {e}"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
