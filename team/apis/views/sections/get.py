from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from team.models import Section
from team.apis.serializers import SectionSerializer


@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])
def get_all_section(request):
    try:
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response({"message": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {
                "message": f"an error occurred while retrieving all sections information {e}"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
