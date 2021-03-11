from django.core.mail import send_mail

from toys.models import Toy


def send_weekly_toys_count(user):
    toys_count= Toy.objects.filter(user= user, is_active=True).count()
    send_mail(
        'Your toys update from Alltoys! ',
        f'You have {toys_count} active toys at the end of this week',
        'info@alltoys.uz',
        [user.email],
        fail_silently= False,
    )