from django.db import models

class Case_study(models.Model):
    study_area = models.CharField(max_length=30)
    description = models.TextField(null=True)

    def __str__(self): 
         return "Case study ("+self.study_area+")"

    def get_all_workshops(self):
        workshops = self.workshop.all()
        return workshops
    
    def get_all_images(self):
        images = self.image.all()
        return images
    
    def get_all_stories(self):
        stories = self.story.all()
        return stories
    

class Workshop(models.Model):
    title = models.CharField(max_length=100)
    case_study = models.ForeignKey(Case_study, on_delete=models.CASCADE, null=True, blank=True, related_name='workshop')
    date = models.DateField()
    upcoming = models.BooleanField()
    venue = models.CharField(max_length=50)
    description = models.TextField()
    coordinator = models.CharField(max_length=50)
    # images = 
    link = models.TextField(null=True, blank=True)

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
    ('training_manual', 'Training_Manual')
)

class Resources(models.Model):
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=30, choices=RESOURCES_CHOICES, default='publication')
    date_of_publishing = models.DateField()
    publisher = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/resource/')
    link = models.URLField(max_length=250, null=True, default='#')
    

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
    position = models.CharField(max_length=40)
    organisation = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/team_member/')

    
    def __str__(self): 
         return self.name + " ("+self.category+")"


    



