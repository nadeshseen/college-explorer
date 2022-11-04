from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class ResearchInterests(models.Model):
    '''
    Model for all Research areas.

    This is class for models/tables which contains every research area that if found during the web-scraping.
    '''
    name = models.CharField(max_length=50)
    info = models.TextField()


class TeacherMany(models.Model):
    '''
    Model for all Teachers.

    This is class for models/tables which contains relevant information regarding each teacher. This model has ManytoManyfiled which is pointed to ResearchInterests Model
    '''
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    citations_all = models.IntegerField(null=True)
    citations_since_2016 = models.IntegerField(null=True)
    hindex_all = models.IntegerField(null=True)
    hindex_since_2016 = models.IntegerField(null=True)
    i10index_all = models.IntegerField(null=True)
    i10index_since_2016 = models.IntegerField(null=True)
    college = models.CharField(max_length=100, null=True)
    links = models.CharField(max_length=200, null=True)

    all_research_areas = models.CharField(max_length=200, null=True)
    research_areas = models.ManyToManyField(ResearchInterests)

    def __str__(self):
        return f"{self.name}"
