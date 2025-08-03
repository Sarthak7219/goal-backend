from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
# from django.core.mail import send_mail
# from django.conf import settings
from core.models import Case_study, Workshop, Resources, TeamMember, Image_Case_Study, Image_Workshop, Stories, HomePage, CollaboratingInstitute, About, Theme, CaseStudyThemeDescription, CaseStudyThemeImage
# from django.contrib.admin.models import LogEntry


# @receiver(post_save)
# def send_email_on_save(sender, instance, created, **kwargs):
        
#     if not isinstance(instance, LogEntry):  # Skip the LogEntry model
#     # Get the list of all models in your app
#         app_models = [Case_study, Workshop, Resources, TeamMember, Image_Case_Study, Image_Workshop, Stories, HomePage, CollaboratingInstitute, About, Theme, CaseStudyThemeDescription, CaseStudyThemeImage]
        
#         # Check if the model is from your desired app(s)
#         if sender in app_models:
#             subject = f'A {sender.__name__} object was created' if created else f'A {sender.__name__} object was updated'
#             message = f'Details of the new/updated object:\n\n{instance}'
#             recipient_list = [settings.RECEIVER_EMAIL]  # email list here
            
#             send_mail(
#                 subject,
#                 message,
#                 settings.DEFAULT_FROM_EMAIL,  # From email
#                 recipient_list,
#                 fail_silently=False,
#             )

@receiver(post_save, sender=HomePage)
@receiver(post_delete, sender=HomePage)
def clear_homepage_cache(sender, instance, **kwargs):
    cache.delete("homepage_data")

@receiver(post_save, sender=About)
@receiver(post_delete, sender=About)
def clear_about_cache(sender, instance, **kwargs):
    cache.delete("about_data")

@receiver(post_save, sender=Stories)
@receiver(post_delete, sender=Stories)
def clear_stories_cache(sender, instance, **kwargs):
    cache.delete("stories_data")

@receiver(post_save, sender=TeamMember)
@receiver(post_delete, sender=TeamMember)
def clear_team_cache(sender, instance, **kwargs):
    cache.delete("team_data")

@receiver(post_save, sender=TeamMember)
@receiver(post_delete, sender=TeamMember)
def clear_team_member_cache(sender, instance, **kwargs):
    cache.delete(f"team_member_{instance.id}")

@receiver(post_save, sender=Workshop)
@receiver(post_delete, sender=Workshop)
def clear_workshop_list_cache(sender, instance, **kwargs):
    cache.delete("workshops_list")

@receiver(post_save, sender=Workshop)
@receiver(post_delete, sender=Workshop)
def clear_workshop_cache(sender, instance, **kwargs):
    cache.delete(f"workshop_{instance.id}")

@receiver(post_save, sender=Case_study)
@receiver(post_delete, sender=Case_study)
def clear_case_studies_cache(sender, instance, **kwargs):
    cache.delete("case_studies_list")

@receiver(post_save, sender=Case_study)
@receiver(post_delete, sender=Case_study)
def clear_case_study_cache(sender, instance, **kwargs):
    cache.delete(f"case_study_{instance.id}")

@receiver(post_save, sender=Resources)
@receiver(post_delete, sender=Resources)
def clear_resources_cache(sender, instance, **kwargs):
    cache.delete("resources_list")

@receiver(post_save, sender=Theme)
@receiver(post_delete, sender=Theme)
def clear_themes_cache(sender, instance, **kwargs):
    cache.delete("themes_list")

@receiver(post_save, sender=Image_Case_Study)
@receiver(post_delete, sender=Image_Case_Study)
def clear_case_study_images_cache(sender, instance, **kwargs):
    case_study_id = instance.case_study.id

    cache_key_pages = f"visit_photos_pages_{case_study_id}"
    cached_pages = cache.get(cache_key_pages, set())

    for page in cached_pages:
        cache_key = f"visit_photos_{case_study_id}_page_{page}"
        cache.delete(cache_key)

    cache.delete(cache_key_pages)

@receiver(post_save, sender=Image_Workshop)
@receiver(post_delete, sender=Image_Workshop)
def clear_workshop_images_cache(sender, instance, **kwargs):
    case_study_id = instance.workshop.case_study.id
   
    cache_key_pages = f"workshop_photos_pages_{case_study_id}"
    cached_pages = cache.get(cache_key_pages, set()) 

    for page in cached_pages:
        cache_key = f"workshop_photos_{case_study_id}_page_{page}"
        cache.delete(cache_key)

    cache.delete(cache_key_pages)

@receiver(post_save, sender=CaseStudyThemeDescription)
@receiver(post_delete, sender=CaseStudyThemeDescription)
def clear_theme_detail_cache_on_description_change(sender, instance, **kwargs):
    cache_key = f"theme_{instance.theme.id}"
    cache.delete(cache_key)

@receiver(post_save, sender=CaseStudyThemeImage)
@receiver(post_delete, sender=CaseStudyThemeImage)
def clear_theme_detail_cache_on_image_change(sender, instance, **kwargs):
    cache_key = f"theme_{instance.theme.id}"
    cache.delete(cache_key)
