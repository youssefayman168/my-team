from django.urls import path
from .views.create import create_contact
from .views.delete import delete_contact, trash_contact
from .views.get import get_contact, get_all_contacts
from .views.update import mark_contact_read, star_contact
from .views.filters import (
    get_seen_contacts,
    get_trashed_contacts,
    get_latest_contacts,
    get_starred_contacts,
)

urlpatterns = [
    path("send-contact/", create_contact),
    path("trash-contact/<int:contact_id>/", trash_contact),
    path("delete-contact/<int:contact_id>/", delete_contact),
    path("get-contact/<int:contact_id>/", get_contact),
    path("get-contacts/", get_all_contacts),
    path("read-contact/<int:contact_id>/", mark_contact_read),
    path("star-contact/<int:contact_id>/", star_contact),
    path("seen-contacts/", get_seen_contacts),
    path("trashed-contacts/", get_trashed_contacts),
    path("latest-contacts/", get_latest_contacts),
    path("starred-contacts/", get_starred_contacts),
]
