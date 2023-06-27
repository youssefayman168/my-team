from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from team.models import Skill


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def update_skill(request, skill_name):
    name = request.data.get("newSkillName")

    if not name:
        return Response(
            {"message": "Please enter a new skill name"}, status.HTTP_400_BAD_REQUEST
        )

    try:
        skill = Skill.objects.get(name=skill_name)
    except Skill.DoesNotExist:
        return Response(
            {"message": "The skill with that name does not exist"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        if name == skill.name:
            return Response(
                {"message": "The new skill name is identical to the current one"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        is_skill_exists = Skill.objects.filter(name=name).exists()
        if is_skill_exists:
            return Response(
                {"message": "The skill with that name already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        skill.name = name
        skill.save()
        return Response(
            {"message": "Skill has updated successfully"}, status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response(
            {"message": f"an error occurred while updating the skill {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
