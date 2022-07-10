from django.db import models

# Create your models here.



class SubjectsModel(models.Model):
    SEM_CHOICES =(
    ("4", "4th"),
    ("5", "5th"),
    ("6", "6th"),
    ("7", "7th"),
    )

    DEF_CHOICES =(
    ("Civil", "Civil"),
    ("Computer", "Computer"),
    ("Marine", "Marine"),
    ("RAC", "RAC"),
    ("POWER", "POWER"),
    ("Electronics", "Electronics"),
    ("Electrical", "Electrical"),
    ("Mechanical", "Mechanical"),
    ("Automobile", "Automobile"),
    )
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length = 20, choices = SEM_CHOICES)
    depermant = models.CharField(max_length = 20, choices = DEF_CHOICES)

    def __str__(self):
        return self.name


class StudentModel(models.Model):
    roll = models.CharField(max_length=6, unique=True)
    passed = models.BooleanField()
    result = models.CharField(max_length=4, blank=True, null=True)
    failed_subjects = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.roll
    