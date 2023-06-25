from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from projects.models import Project
from team.models import Section, Skill


@api_view(
    [
        "POST",
    ]
)
@permission_classes([permissions.IsAdminUser])
def create_project(request):
    data = request.data

    if not data:
        return Response(
            {"message": "You must provide data to create a project"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    project_name = data.get("projectName")
    member_name = data.get("memberName")
    client_name = data.get("clientName")
    finished_date = data.get("finishedDate")
    skills = data.get("skills")
    belongs_to = data.get("section")
    project_photo = request.FILES.get("projectPhoto")
    certian_skills = []

    if not project_name or project_name == "":
        return Response(
            {"message": "You must enter a name for the project"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not member_name or member_name == "":
        return Response(
            {"message": "You must enter the member name"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not client_name or client_name == "":
        return Response(
            {"message": "You must enter the client name"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not finished_date or finished_date == "":
        return Response(
            {"message": "You must enter a finsihed date"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not skills or len(skills) == 0:
        return Response(
            {"message": "You must enter a skills list"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not belongs_to or belongs_to == "":
        return Response(
            {"message": "You must sepecify a section for the project"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not project_photo:
        return Response(
            {"message": "You must enter a project photo"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        for skill in skills:
            picked_skill = Skill.objects.get_or_create(name=skill)
            certian_skills.append(picked_skill)
    except Exception as e:
        return Response(
            {"message": f"an error occured while verifying the skills {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        section = Section.objects.get(name=belongs_to)
    except Section.DoesNotExist:
        return Response(
            {"message": "Could not find a section with that name"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        Project.objects.create(
            project_name=project_name,
            member_name=member_name,
            client_name=client_name,
            skills=certian_skills,
            finished_date=finished_date,
            belongs_to=section,
            project_photo=project_photo,
        )
        return Response(
            {"message": "Project successfully created"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"message": f"an error occured while creating the project"},
            status=status.HTTP_400_BAD_REQUEST,
        )
