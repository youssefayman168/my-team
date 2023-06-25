from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from team.models import Skill, Section, Memeber
from email_validator import validate_email, EmailNotValidError


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def update_member(request, member_id):
    data = request.data

    try:
        member = Memeber.objects.get(pk=member_id)
    except Memeber.DoesNotExist:
        return Response(
            {"message": "Member does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    member_name = data.get("memberName")
    posistion = data.get("posistion")
    phone_number = data.get("phoneNumber")
    skills = data.get("skills")
    picture = request.FILES.get("memberPicture")
    email = data.get("email")
    belongs_to = data.get("belongsTo")
    # * a flag indicating whether any field has updated or not
    is_updated = False

    try:
        if member_name and member_name != member.member_name:
            member.member_name = member_name
            is_updated = True

        if posistion and posistion != member.posistion:
            member.posistion = posistion
            is_updated = True

        if phone_number and phone_number != member.phone_number:
            member.phone_number = phone_number
            is_updated = True

        if skills:
            for skill in skills:
                picked_skill = Skill.objects.get_or_create(name=skill)
                member.skills.add(picked_skill)
                is_updated = True

        if picture and picture != member.picture:
            member.picture = picture
            is_updated = True

        if email:
            try:
                is_valid_email = validate_email(email)
            except EmailNotValidError:
                return Response(
                    {"message": "Email is not valid"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if email != member.email:
                member.email = email
                is_updated = True

        if belongs_to and belongs_to != member.belongs_to.name:
            try:
                section = Section.objects.get(name=belongs_to)
            except Section.DoesNotExist:
                return Response(
                    {"message": "Could not find a section with this name"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            member.belongs_to = section
            is_updated = True

        if is_updated:
            member.save(force_update=True)
            return Response(
                {"message": "Member updated successfully"}, status=status.HTTP_200_OK
            )
        return Response({"message": "Nothing to update"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": f"Something went wrong while trying to update the member {e}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
