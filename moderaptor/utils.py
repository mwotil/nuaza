from django.conf import settings as main_settings
from moderaptor import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context, RequestContext

def is_moderator(user):
    if len(settings.MODERATORS_GROUPS_IDS) == 0:
        raise Exception, 'settings.MODERATORS_GROUPS_IDS is empty. Check your settings.'
    if not type(settings.MODERATORS_GROUPS_IDS) is list:
        raise Exception, 'Argument is not a User instance.'
    if user.is_active:
        if user.groups.filter(id__in=settings.MODERATORS_GROUPS_IDS):
            return True
    return False


def can_report(user):
    if settings.SIGNED_IN_ONLY and not user.is_active:
        return False
    return True
    
    
# ??? not implemented yet
def send_notification(report, action='add'):
    if settings.EMAIL_NOTIFY:
        message = get_template('moderaptor/email.html').render(Context({'report': report,}))
        users = User.objects.filter(groups__id__in=settings.MODERATORS_GROUPS_IDS)
        for user in users:
            send_mail(settings.EMAIL_SUBJECT, message, main_settings.DEFAULT_FROM_EMAIL, [user.email], False)
        return True
    return False
    