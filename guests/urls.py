from django.urls import path

from guests.views import (GuestListView, dashboard, export_guests, invitation,
                          invitation_email, invitation_email_preview,
                          invitation_email_test, rsvp_confirm,
                          save_the_date_preview, save_the_date_random,
                          send_all_invitations_view, test_email)

urlpatterns = [
    path("guests", GuestListView.as_view(), name='guest-list'),
    path("dashboard", dashboard, name='dashboard'),
    path("guests/export", export_guests, name='export-guest-list'),
    path("invite/<str:invite_id>", invitation, name='invitation'),
    path("invite-email/<str:invite_id>/", invitation_email_preview, name='invitation-email'),
    path("send-invites-email/<str:invite_id>/", invitation_email, name='send_invites'),
    path("invite-email-test/<str:invite_id>/", invitation_email_test, name='invitation-email-test'),
    path("save-the-date/", save_the_date_random, name='save-the-date-random'),
    path("save-the-date/<str:template_id>)/", save_the_date_preview, name='save-the-date'),
    path("email-test/(<str:template_id>)/", test_email, name='test-email'),
    path("send-invites", send_all_invitations_view, name='send_all_invitations_test_emails'),
    path("rsvp/confirm/(<str:invite_id>)/", rsvp_confirm, name='rsvp-confirm'),
]
