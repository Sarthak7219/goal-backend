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
    



