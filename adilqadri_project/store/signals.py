from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.crypto import get_random_string

@receiver(post_save, sender=User)
def send_verification_email(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        token = get_random_string(20)
        instance.profile.email_verification_token = token
        instance.profile.save()

        current_site = get_current_site(None)
        verification_link = f"http://{current_site.domain}{reverse('email_verify', args=[urlsafe_base64_encode(force_bytes(instance.pk)), token])}"

        subject = 'Verify your email address'
        message = render_to_string('registration/email_verification_email.html', {
            'user': instance,
            'verification_link': verification_link,
        })
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])
</create_file>
