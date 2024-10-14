from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from core.models import Case_study, Workshop, Resources, TeamMember, Image_Case_Study, Image_Workshop, Stories, HomePage, CollaboratingInstitute, About, Theme, CaseStudyThemeDescription, CaseStudyThemeImage
from django.contrib.admin.models import LogEntry


@receiver(post_save)
def send_email_on_save(sender, instance, created, **kwargs):
        
    if not isinstance(instance, LogEntry):  # Skip the LogEntry model
    # Get the list of all models in your app
        app_models = [Case_study, Workshop, Resources, TeamMember, Image_Case_Study, Image_Workshop, Stories, HomePage, CollaboratingInstitute, About, Theme, CaseStudyThemeDescription, CaseStudyThemeImage]
        
        # Check if the model is from your desired app(s)
        if sender in app_models:
            subject = f'A {sender.__name__} object was created' if created else f'A {sender.__name__} object was updated'
            message = f'Details of the new/updated object:\n\n{instance}'
            recipient_list = ['sarthakrangari788@gmail.com']  # email list here
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,  # From email
                recipient_list,
                fail_silently=False,
            )