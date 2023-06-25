from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from team.models import Skill, Section, Memeber
from email_validator import validate_email, EmailNotValidError


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_member(request):
    data = request.data

    if not data:
        return Response(
            {"message": "No data to create member"}, status=status.HTTP_400_BAD_REQUEST
        )

    member_name = data.get("memberName")
    position = data.get("position")
    phone_number = data.get("phoneNumber")
    skills = data.get("skills")
    picture = request.FILES.get("memberPicture")
    email = data.get("email")
    belongs_to = data.get("belongsTo")
    certian_skills = []

    if not member_name:
        return Response(
            {"message": "Member name is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not position:
        return Response(
            {"message": "Position is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not phone_number:
        return Response(
            {"message": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not skills or len(skills) == 0:
        return Response(
            {"message": "You must specify at least one skill"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not picture:
        return Response(
            {"message": "Member should have a picture"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not email:
        return Response(
            {"message": "Member should have an email"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not belongs_to:
        return Response(
            {"message": "Member should have a section that belongs to"},
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
        is_email_valid = validate_email(email)
    except EmailNotValidError:
        return Response(
            {"message": "email validation failed"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        section = Section.objects.get(name=belongs_to)
    except Section.DoesNotExist:
        return Response(
            {"message": "Could not find a section with that name"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        Memeber.objects.create(
            member_name=member_name,
            position=position,
            phone_number=phone_number,
            skills=certian_skills,
            picture=picture,
            email=email,
            belongs_to=section,
        )
        return Response(
            {"message": "Successfully created a member"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"message": f"an error occured while creating the member {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
