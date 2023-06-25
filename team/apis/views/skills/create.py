from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from team.models import Skill


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_skill(request):
    name = request.data.get("skillName")
    is_skill_exists = Skill.objects.filter(name=name).exists()
    try:
        if is_skill_exists:
            return Response(
                {"message": "There's already a skill with that name"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Skill.objects.create(name=name)
        return Response(
            {"message": "skill created successfully"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"message": f"an error occurred while creating the skill {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
