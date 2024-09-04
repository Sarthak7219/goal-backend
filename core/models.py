from django.db import models
from django.core.exceptions import ValidationError

class Case_study(models.Model):
    study_area = models.CharField(max_length=130)
    description = models.TextField(null=True)
    country = models.CharField(max_length=50, null=True)

    def __str__(self): 
         return "Case study ("+self.study_area+")"

    def get_all_workshops(self):
        workshops = self.workshop.all()
        return workshops
    
    def get_all_images(self):
        images = self.images.all()
        return images
    
    def get_all_stories(self):
        stories = self.story.all()
        return stories
    

MODE_CHOICES = (
    ('offline', 'Offline'),
    ('online', 'Online')
)

class Workshop(models.Model):
    title = models.CharField(max_length=100)
    case_study = models.ForeignKey(Case_study, on_delete=models.CASCADE, null=True, blank=True, related_name='workshop')
    date = models.DateField()
    
    venue = models.CharField(max_length=50)
    description = models.TextField()
    organised_by = models.CharField(max_length=150,null=True, blank=True)
    
    link = models.TextField(null=True, blank=True)
    speakers = models.CharField(max_length=200,null=True, blank=True)
    key_takeaways = models.TextField(null=True, blank=True)
    mode = models.CharField(max_length=30, choices=MODE_CHOICES, default='offline')

    def __str__(self):
        return self.title[:50]

    def get_all_workshop_images(self):
        images = self.images.all()
        return images
    
    def get_workshop_case_study(self):
        case_study = self.case_study
        return case_study

    def get_all_related_workshops(self):
        case_study = self.case_study
        workshops = case_study.get_all_workshops
        return workshops
    

# class Image(models.Model):
#     case_study = models.ForeignKey(Case_study, on_delete=models.CASCADE, null=True, blank=True, related_name='workshop')


RESOURCES_CHOICES = (
    ('publication', 'Publication'),
    ('training_tool', 'Training Tool')
)

class Resources(models.Model):
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=30, choices=RESOURCES_CHOICES, default='publication')
    date_of_publishing = models.DateField()
    publisher = models.CharField(max_length=25)
    link = models.URLField(max_length=250, null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/resources/', blank=True, null=True)
    

    def __str__(self): 
         return self.category
    


TEAM_MEMBER_CHOICES = (
    ('collaborator', 'Collaborator'),
    ('research_associate', 'Research_Associate'),
    ('community_trainer', 'Community_Trainer'),
    ('intern', 'Intern'),
    ('student', 'Students'),
)

class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=TEAM_MEMBER_CHOICES)
    position = models.CharField(max_length=40,null=True,blank=True)
    organisation = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    apn_profile_link =  models.TextField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/team_member/', default='images/team_member/default.jpg')
    bg_image=models.ImageField(upload_to='images/team_member/',null=True,blank=True)
    website_link =  models.TextField(null=True, blank=True)
    
    def __str__(self): 
         return self.name + " ("+self.category+")"

class Image_Case_Study(models.Model):
    case_study=models.ForeignKey(Case_study,on_delete=models.CASCADE,related_name='images',blank=True,null=True)
    image=models.ImageField(upload_to='images/case_study/',default=True)
    caption=models.TextField(max_length=30,blank=True,null=True)
    date=models.DateField(null=True,blank=True)


class Image_Workshop(models.Model):
    workshop=models.ForeignKey(Workshop,on_delete=models.CASCADE,related_name='images',blank=True,null=True)
    image=models.ImageField(upload_to='images/workshop/',default=True)
    caption=models.TextField(max_length=30,blank=True,null=True)
    date=models.DateField(null=True,blank=True)


class Stories(models.Model):
    link = models.TextField(null=True, blank=True)
    date=models.DateField(null=True,blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)



class HomePage(models.Model):
    map_image = models.ImageField(upload_to='images/general/')

    def save(self, *args, **kwargs):
        if not self.pk and HomePage.objects.exists():
            raise ValidationError('There can only be one HomePage instance')
        return super(HomePage, self).save(*args, **kwargs)

    def __str__(self):
        return "Home Page Content"

class CollaboratingInstitute(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='images/logos/')
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='institutes')
    

    def __str__(self):
        return self.name


class About(models.Model):
    abstract = models.TextField()
    description = models.TextField()
    img1 = models.ImageField(null=True, upload_to='images/about/')
    img2 = models.ImageField(null=True, upload_to='images/about/')
    img3 = models.ImageField(null=True, upload_to='images/about/')
    img4 = models.ImageField(null=True, upload_to='images/about/')

    def __str__(self):
        return "About Page"

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValueError('Only one About instance is allowed.')
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"



class Theme(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
    
class CaseStudyThemeDescription(models.Model):
    case_study = models.ForeignKey(Case_study, on_delete=models.CASCADE, related_name='case_study_themes')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='case_study_themes')
    description = models.TextField()
    
    def __str__(self):
        return f"{self.case_study.study_area} - {self.theme.title}"

# class Image_Theme(models.Model):
#     theme_case_study = models.ForeignKey(CaseStudyThemeDescription, on_delete=models.CASCADE)
#     image=models.ImageField(upload_to='images/theme/',default=True)
#     caption=models.TextField(max_length=30,blank=True,null=True)
#     date=models.DateField(null=True,blank=True)

class CaseStudyThemeImage(models.Model):
    case_study = models.ForeignKey(Case_study, on_delete=models.CASCADE, related_name='case_study_themes_image')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='case_study_themes_image')
    image=models.ImageField(upload_to='images/theme/',default=True)
    caption=models.TextField(max_length=30,blank=True,null=True)
    date=models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.case_study.study_area} - {self.theme.title}"
    



