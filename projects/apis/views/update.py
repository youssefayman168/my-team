from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from projects.models import Project
from team.models import Section, Skill


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def update_project(request, project_id):
    data = request.data

    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return Response(
            {"message": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    project_name = data.get("projectName")
    member_name = data.get("memberName")
    client_name = data.get("clientName")
    finished_date = data.get("finishedDate")
    skills = data.get("skills")
    belongs_to = data.get("section")
    project_photo = request.FILES.get("projectPhoto")
    # * a flag indicating whether any field has updated or not
    is_updated = False

    try:
        if project_name and project_name != project.project_name:
            project.project_name = project_name
            is_updated = True

        if member_name and member_name != project.member_name:
            project.member_name = member_name
            is_updated = True

        if client_name and client_name != project.client_name:
            project.client_name = client_name
            is_updated = True

        if finished_date and finished_date != project.finished_date:
            project.finished_date = finished_date
            is_updated = True

        if project_photo and project_photo != project.project_photo:
            project.project_photo = project_photo
            is_updated = True

        if skills:
            for skill in skills:
                picked_skill = Skill.objects.get_or_create(name=skill)
                project.skills.add(picked_skill)
                is_updated = True

        if belongs_to and belongs_to != project.belongs_to.name:
            try:
                section = Section.objects.get(name=belongs_to)
            except Section.DoesNotExist:
                return Response(
                    {"message": "Could not find a section with this name"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            project.belongs_to = section
            is_updated = True

        if is_updated:
            project.save(force_update=True)
            return Response(
                {"message": "Project updated successfully"}, status=status.HTTP_200_OK
            )
        return Response({"message": "Nothing to update"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": f"Something went wrong while trying to update the project {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
