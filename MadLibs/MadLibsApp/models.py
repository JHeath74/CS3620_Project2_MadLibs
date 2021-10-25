from django.db import models


# Create your models here.
#Accept
class MadLibsStorage(models.Model):

    def __str__(self):
        return self.MadLibsName

    MadLibsName = models.CharField(max_length=20)
    MadLibsToDisplay = models.CharField(max_length=500)


class MadLibsUserInput(models.Model):

    # def __str__(self):
    #     return self.ID

    ID = models.IntegerField()
    Noun = models.CharField(max_length=25)
    Noun2 = models.CharField(max_length=25)
    Noun3 = models.CharField(max_length=25)
    Person = models.CharField(max_length=25)
    Place = models.CharField(max_length=25)
    Thing = models.CharField(max_length=25)
    Adjective = models.CharField(max_length=25)
