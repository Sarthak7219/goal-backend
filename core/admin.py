from django.contrib import admin
from .models import *

admin.site.register(Workshop)
admin.site.register(Case_study)
admin.site.register(Resources)
admin.site.register(TeamMember)
admin.site.register(Image_Case_Study)
admin.site.register(Image_Workshop)
admin.site.register(Stories)

class CollaboratingInstituteInline(admin.TabularInline):
    model = CollaboratingInstitute
    extra = 1

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    inlines = [CollaboratingInstituteInline]
    list_display = ('id',)

    def has_add_permission(self, request):
        # Disable the add button if there is already a HomePage instance
        return not HomePage.objects.exists()

    def change_view(self, request, object_id=None, form_url='', extra_context=None):
        if HomePage.objects.exists() and not object_id:
            # Redirect to the edit page of the existing HomePage instance
            existing_homepage = HomePage.objects.first()
            return super(HomePageAdmin, self).change_view(request, str(existing_homepage.id))
        return super(HomePageAdmin, self).change_view(request, object_id, form_url, extra_context)
    
    def has_delete_permission(self, request, obj=None):
        # Disallow deleting the About instance
        return False


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Disallow adding new About instances if one already exists
        return not About.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Disallow deleting the About instance
        return False
    

class CaseStudyThemeDescriptionInline(admin.TabularInline):
    model = CaseStudyThemeDescription
    extra = 1
    fields = ['case_study', 'description']  # Exclude the 'theme' field from display

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "theme":
            # Set the current theme in the inline form
            kwargs["initial"] = request.resolver_match.kwargs['object_id']
            kwargs["queryset"] = Theme.objects.filter(pk=request.resolver_match.kwargs['object_id'])
            kwargs["disabled"] = True  # Disable the theme selection to make it read-only
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_formset(self, request, form, formset, change):
        # Automatically set the theme before saving
        instances = formset.save(commit=False)
        for instance in instances:
            instance.theme = form.instance
            instance.save()
        formset.save_m2m()


class CaseStudyThemeImageInline(admin.StackedInline):
    model = CaseStudyThemeImage
    extra = 1
    fields = ['case_study', 'image', 'caption', 'date']  # Exclude the 'theme' field from display

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "theme":
            # Set the current theme in the inline form
            kwargs["initial"] = request.resolver_match.kwargs['object_id']
            kwargs["queryset"] = Theme.objects.filter(pk=request.resolver_match.kwargs['object_id'])
            kwargs["disabled"] = True  # Disable the theme selection to make it read-only
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_formset(self, request, form, formset, change):
        # Automatically set the theme before saving
        instances = formset.save(commit=False)
        for instance in instances:
            instance.theme = form.instance
            instance.save()
        formset.save_m2m()

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    inlines = [CaseStudyThemeDescriptionInline, CaseStudyThemeImageInline]