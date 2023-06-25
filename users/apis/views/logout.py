from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def logout(request):
    refresh = request.data.get("refresh")

    if not refresh:
        return Response(
            {"message": "You must provide a refresh token"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        token = RefreshToken(token=refresh)
        token.blacklist()
        return Response(
            {"message": "You have successfully logged out"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"message": f"an error occurred while trying to log you out {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
