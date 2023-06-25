from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from team.models import Section


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_section(request):
    name = request.data.get("sectionName")
    is_section_exists = Section.objects.filter(name=name).exists()
    try:
        if is_section_exists:
            return Response(
                {"message": "There's already a section with that name"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Section.objects.create(name=name)
        return Response(
            {"message": "section created successfully"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"message": f"an error occurred while creating the section {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
