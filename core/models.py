from django.db import models
from django.core.exceptions import ValidationError
import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils.timezone import now

class Case_study(models.Model):
    study_area = models.CharField(max_length=130)
    description = models.TextField(null=True)
    country = models.CharField(max_length=50, null=True)
    thumbnail = models.ImageField(upload_to='images/case_study/thumbnails/', null=True, blank=True)
    map_image = models.ImageField(upload_to='images/case_study/maps/', null=True, blank=True)
    def __str__(self): 
         return "Case study ("+self.study_area+")"

    def get_all_workshops(self):
        workshops = self.workshop.all()
        return workshops
        
    #Optimize before saving
    def save(self, *args, **kwargs):
        if self.thumbnail:
            img = Image.open(self.thumbnail)
            img_format = img.format 
            
            img.thumbnail((800, 800), Image.LANCZOS)

            img_io = BytesIO()
            img.save(img_io, format=img_format, quality=95, optimize=True)
            self.thumbnail = ContentFile(img_io.getvalue(), name=self.thumbnail.name)
        super().save(*args, **kwargs)


MODE_CHOICES = (
    ('offline', 'In Person'),
    ('online', 'Online'),
    ('hybrid','Hybrid')
)

class Workshop(models.Model):
    title = models.CharField(max_length=1000)
    case_study = models.ForeignKey(Case_study, on_delete=models.CASCADE, null=True, blank=True, related_name='workshop')
    date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    venue = models.CharField(max_length=500)
    description = models.TextField()
    organised_by = models.CharField(max_length=150,null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    speakers = models.CharField(max_length=200,null=True, blank=True)
    key_takeaways = models.TextField(null=True, blank=True)
    mode = models.CharField(max_length=30, choices=MODE_CHOICES, default='offline')
    thumbnail = models.ImageField(upload_to='images/workshop/thumbnails/', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    lead_institution = models.CharField(max_length=200,null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/workshops/', blank=True, null=True)
    def __str__(self):
        return self.title[:50]
    
    def get_workshop_case_study_name(self):
        case_study_name = self.case_study.study_area
        return case_study_name if case_study_name else ""

    def get_all_related_workshops(self):
        case_study = self.case_study
        workshops = case_study.get_all_workshops
        return workshops
    
    def save(self, *args, **kwargs):
        if self.thumbnail:
            img = Image.open(self.thumbnail)
            img_format = img.format 
            
            img.thumbnail((800, 800), Image.LANCZOS)

            img_io = BytesIO()
            img.save(img_io, format=img_format, quality=95, optimize=True)

            filename = os.path.basename(self.thumbnail.name)
            self.thumbnail.save(filename, ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.pdf:
            if os.path.isfile(self.pdf.path):
                os.remove(self.pdf.path)
        super().delete(*args, **kwargs)
    
RESOURCES_CHOICES = (
    ('publication', 'Publication'),
    ('training_tool', 'Training Tool'),
    ('flashcard', 'Flashcard'),
    ('map', 'Map')
)

class Resources(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=RESOURCES_CHOICES, default='publication')
    date_of_publishing = models.DateField(verbose_name="Date")
    publisher = models.CharField(max_length=25, verbose_name="Publisher/Source")
    link = models.URLField(max_length=250, null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/resources/', blank=True, null=True)
    image = models.ImageField(upload_to='images/resource/',  blank=True, null=True)

    def clean(self):
        if self.category == "flashcard" or self.category == "map":
            if not self.image:
                raise ValidationError("Flashcard/Map must have an image")
            if self.pdf or self.link:
                raise ValidationError("Flashcard/Map only supports image. For link/pdf please select other category")
        else:
            if self.image:
                raise ValidationError("Resource only supports pdf/link. For image please select Flashcard or Map")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self): 
         return f"{self.category} - {self.title}"
    def delete(self, *args, **kwargs):
        if self.pdf:
            if os.path.isfile(self.pdf.path):
                os.remove(self.pdf.path)
        super().delete(*args, **kwargs)

TEAM_MEMBER_CHOICES = (
    ('collaborator', 'Collaborator'),
    ('research_associate', 'Research Associate'),
    ('community_trainer', 'Community Knowledge Partner'),
    ('intern', 'Intern'),
    ('student', 'Classroom Integration Partner'),
    ('icimod_huc_partners', 'HUC-ICIMOD Partner'),
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
    
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img_format = img.format  
            
            img.thumbnail((800, 800), Image.LANCZOS)

            img_io = BytesIO()
            img.save(img_io, format=img_format, quality=95, optimize=True)
            self.image = ContentFile(img_io.getvalue(), name=self.image.name)

        super().save(*args, **kwargs)
    
class Image_Case_Study(models.Model):
    case_study=models.ForeignKey(Case_study,on_delete=models.CASCADE,related_name='images',blank=True,null=True)
    image=models.ImageField(upload_to='images/case_study/',default=True)
    caption=models.TextField(max_length=50,blank=True,null=True)
    date=models.DateField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img_format = img.format  
            
            img.thumbnail((800, 800), Image.LANCZOS)

            img_io = BytesIO()
            img.save(img_io, format=img_format, quality=95, optimize=True)
            self.image = ContentFile(img_io.getvalue(), name=self.image.name)

        super().save(*args, **kwargs)


class Image_Workshop(models.Model):
    workshop=models.ForeignKey(Workshop,on_delete=models.CASCADE,related_name='images',blank=True,null=True)
    image=models.ImageField(upload_to='images/workshop/',default=True)
    caption=models.TextField(max_length=50,blank=True,null=True)
    date=models.DateField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img_format = img.format  
            
            img.thumbnail((800, 800), Image.LANCZOS)

            img_io = BytesIO()
            img.save(img_io, format=img_format, quality=95, optimize=True)
            self.image = ContentFile(img_io.getvalue(), name=self.image.name)

        super().save(*args, **kwargs)


class Stories(models.Model):
    link = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/workshops/', null=True, blank=True)
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


class CaseStudyThemeImage(models.Model):
    case_study = models.ForeignKey(Case_study, on_delete=models.CASCADE, related_name='case_study_themes_image')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='case_study_themes_image')
    image=models.ImageField(upload_to='images/theme/',default=True)
    caption=models.TextField(max_length=50,blank=True,null=True)
    date=models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.case_study.study_area} - {self.theme.title}"
    
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img_format = img.format  
            
            img.thumbnail((800, 800), Image.LANCZOS)

            img_io = BytesIO()
            img.save(img_io, format=img_format, quality=95, optimize=True)
            self.image = ContentFile(img_io.getvalue(), name=self.image.name)

        super().save(*args, **kwargs)
    



