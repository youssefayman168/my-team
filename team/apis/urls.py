from django.urls import path
from .views.create import create_member
from .views.get import get_member, get_members_bysection
from .views.delete import delete_member
from .views.update import update_member
from .views.sections.create import create_section
from .views.sections.get import get_all_sections
from .views.skills.get import get_all_skills
from .views.skills.create import create_skill
from .views.skills.update import update_skill


urlpatterns = [
    path("create-member/", create_member),
    path("get-member/<int:member_id>/", get_member),
    path("get-members/<int:section_name>/", get_members_bysection),
    path("update-member/<int:member_id>/", update_member),
    path("delete-member/<int:member_id>/", delete_member),
    path("create-section/", create_section),
    path("get-sections/", get_all_sections),
    path("create-skill/", create_skill),
    path("update-skill/<str:skill_name>/", update_skill),
    path("get-skills/", get_all_skills),
]
