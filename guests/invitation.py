import os
from datetime import datetime
from email.mime.image import MIMEImage

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse

from guests.models import MEALS, Party

INVITATION_TEMPLATE = 'guests/email_templates/invitation.html'


def guess_party_by_invite_id_or_404(invitation_id):
    print("TESTING INVITE ID")
    return Party.objects.get(invitation_id=invitation_id)

def get_invitation_context(party):
    return {
        'title': "Wedding",
        'main_image': 'bride-groom.png',
        'main_color': '#fff3e8',
        'font_color': '#666666',
        'page_title': "Bryton and Chloe - You're Invited!",
        'preheader_text': "You are invited!",
        'invitation_id': party.invitation_id,
        'party': party,
        'meals': MEALS,
    }


def send_invitation_email(party, test_only=False, recipients=None):
    if recipients is None:
        recipients = party.guest_emails
        print(recipients)
    if not recipients:
        print ('===== WARNING: no valid email addresses found for {} ====='.format(party))
        return

    context = get_invitation_context(party)
    context['email_mode'] = True
    context['site_url'] = settings.WEDDING_WEBSITE_URL
    context['couple'] = settings.BRIDE_AND_GROOM
    template_html = render_to_string(INVITATION_TEMPLATE, context=context)
    template_text = f"You're invited to Bryton and Chloe's wedding. To view this invitation, visit {reverse('invitation', args=[context['invitation_id']])} in any browser."
    subject = "You're invited"
    # https://www.vlent.nl/weblog/2014/01/15/sending-emails-with-embedded-images-in-django/
    msg = EmailMultiAlternatives(subject, template_text, settings.DEFAULT_WEDDING_FROM_EMAIL, recipients,
                                 cc=settings.WEDDING_CC_LIST,
                                 reply_to=[settings.DEFAULT_WEDDING_REPLY_EMAIL])
    msg.attach_alternative(template_html, "text/html")
    msg.mixed_subtype = 'related'
    for filename in (context['main_image'], ):
        attachment_path = os.path.join(os.path.dirname(__file__), 'static', 'invitation', 'images', filename)
        with open(attachment_path, "rb") as image_file:
            msg_img = MIMEImage(image_file.read())
            msg_img.add_header('Content-ID', '<{}>'.format(filename))
            msg.attach(msg_img)

    print(f"sending invitation to {party.name}")
    if test_only is False:
        print("SENDING")
        msg.send()


def send_all_invitations(test_only, mark_as_sent):
    to_send_to = Party.in_default_order().filter(is_invited=True).exclude(is_attending=False)
    for party in to_send_to:
        send_invitation_email(party, test_only=False, recipients=None)
        if mark_as_sent:
            party.invitation_sent = datetime.now()
            party.save()
