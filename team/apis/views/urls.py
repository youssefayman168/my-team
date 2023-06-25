from django.urls import path
from .create import create_member
from .get import get_member, get_members_bysection

urlpatterns = [
    path("create-member/", create_member),
    path("get-member/<int:member_id>/", get_member),
    path("get-member/<int:section_name>/", get_members_bysection),
]
