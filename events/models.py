from os import terminal_size
from typing import Collection

from django.db import models
from django.db.models.fields.files import FieldFile


# Create your models here.
INT_CHOICES = (
    ("college", "college"),
    ("school", "school"),
    
  
)
class RoboPresetation(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    college = models.CharField(max_length=200,default="")
    teamname = models.CharField(max_length=200,default=" ")

    name1 = models.CharField(max_length=20,default=" ")
    email1 = models.EmailField( max_length=254)
    phone1 = models.CharField(max_length=12,default=" ")
    branch1 = models.CharField(max_length=50,default=" ")
    semester1 = models.CharField(null=True,blank=True,default=" ",max_length=3)
    rollno1 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id1 = models.FileField(upload_to ='RoboPresentation/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254)
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='RoboPresentation/',blank=True,null=True)

    name3 = models.CharField(max_length=20,default=" ")
    email3 = models.EmailField( max_length=254,null=True,blank=True)
    phone3 = models.CharField(null=True,blank=True,default="",max_length=12)
    branch3 = models.CharField(max_length=50,default=" ")
    semester3 = models.CharField(null=True,blank=True,default="",max_length=3)
    rollno3 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id3 = models.FileField(upload_to ='RoboPresentation/',blank=True,null=True)

    def __str__(self):
        return self.teamname + " " +self.college
    
class CECJHACKATHON (models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    college = models.CharField(max_length=200,default="")
    teamname = models.CharField(max_length=200,default=" ")

    name1 = models.CharField(max_length=20,default=" ")
    email1 = models.EmailField( max_length=254)
    phone1 = models.CharField(max_length=12,default=" ")
    branch1 = models.CharField(max_length=50,default=" ")
    semester1 = models.CharField(null=True,blank=True,default=" ",max_length=3)
    rollno1 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id1 = models.FileField(upload_to ='CECJHACKATHON/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254)
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='CECJHACKATHON/',blank=True,null=True)
    
    def __str__(self):
        return self.teamname + " " +self.college

class CecJInovationidea(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    college = models.CharField(max_length=200,default="")
    teamname = models.CharField(max_length=200,default=" ")

    name1 = models.CharField(max_length=20,default=" ")
    email1 = models.EmailField( max_length=254)
    phone1 = models.CharField(max_length=12,default=" ")
    branch1 = models.CharField(max_length=50,default=" ")
    semester1 = models.CharField(null=True,blank=True,default=" ",max_length=3)
    rollno1 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id1 = models.FileField(upload_to ='CecJInovationidea/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254)
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='CecJInovationidea/',blank=True,null=True)
    
    def __str__(self):
        return self.teamname + " " +self.college

class CGCCODATHON(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    branch_class = models.CharField(max_length=50,default=" ")
    semester = models.IntegerField(null=True,blank=True)
    roll_no = models.IntegerField(null=True,blank=True)
    id1 = models.FileField(upload_to='CGCCODATHON/')
    def __str__(self):
        return self.name+" "+self.college_school

class Aiworkshop(models.Model):
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    id1 = models.FileField(upload_to='Aiworkshop/')
    def __str__(self):
        return self.name+" "+self.college_school

class Cyberworkshop(models.Model):
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    id1 = models.FileField(upload_to='Cyberworkshop/')
    def __str__(self):
        return self.name+" "+self.college_school


class TechQuiz(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    branch_class = models.CharField(max_length=50,default=" ")
    semester = models.IntegerField(null=True,blank=True)
    roll_no = models.IntegerField(null=True,blank=True)
    id1 = models.FileField(upload_to='TechQuiz/')
    def __str__(self):
        return self.name+" "+self.college_school

class Autocad(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    branch_class = models.CharField(max_length=50,default=" ")
    semester = models.IntegerField(null=True,blank=True)
    roll_no = models.IntegerField(null=True,blank=True)
    id1 = models.FileField(upload_to='Autocad/')
    def __str__(self):
        return self.name+" "+self.college_school

class ArdunioPiChallenge(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    college = models.CharField(max_length=200,default="")
    teamname = models.CharField(max_length=200,default=" ")

    name1 = models.CharField(max_length=20,default=" ")
    email1 = models.EmailField( max_length=254)
    phone1 = models.CharField(max_length=12,default=" ")
    branch1 = models.CharField(max_length=50,default=" ")
    semester1 = models.CharField(null=True,blank=True,default=" ",max_length=3)
    rollno1 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id1 = models.FileField(upload_to ='ArduinoChallenge/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254)
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='ArduinoChallenge/',blank=True,null=True)
    def __str__(self):
        return self.teamname + " " +self.college

class TechnicalPresentation(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    branch_class = models.CharField(max_length=50,default=" ")
    semester = models.IntegerField(null=True,blank=True)
    roll_no = models.IntegerField(null=True,blank=True)
    id1 = models.FileField(upload_to='TechnicalPresentationEce/')
    def __str__(self):
        return self.name+" "+self.college_school


class ProjectDisplay(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    college = models.CharField(max_length=200,default="")
    teamname = models.CharField(max_length=200,default=" ")
    projectname = models.CharField(max_length=100,default=" ")
    name1 = models.CharField(max_length=20,default=" ")
    email1 = models.EmailField( max_length=254)
    phone1 = models.CharField(max_length=12,default=" ")
    branch1 = models.CharField(max_length=50,default=" ")
    semester1 = models.CharField(null=True,blank=True,default=" ",max_length=3)
    rollno1 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id1 = models.FileField(upload_to ='ProjectDisplay/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254)
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='ProjectDisplay/',blank=True,null=True)
    def __str__(self):
        return self.teamname + " " +self.college


    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    college = models.CharField(max_length=200,default="")
    teamname = models.CharField(max_length=200,default=" ")

    name1 = models.CharField(max_length=20,default=" ")
    email1 = models.EmailField( max_length=254)
    phone1 = models.CharField(max_length=12,default=" ")
    branch1 = models.CharField(max_length=50,default=" ")
    semester1 = models.CharField(null=True,blank=True,default=" ",max_length=3)
    rollno1 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id1 = models.FileField(upload_to ='Rangoli/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254)
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='Rangoli/',blank=True,null=True)

    def __str__(self):
        return self.name1 + " " +self.college

class CollageMaking(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    branch_class = models.CharField(max_length=50,default=" ")
    semester = models.IntegerField(null=True,blank=True)
    roll_no = models.IntegerField(null=True,blank=True)
    id1 = models.FileField(upload_to='CollageMaking/')
    def __str__(self):
        return self.name+" "+self.college_school

class Rangoli(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    branch_class = models.CharField(max_length=50,default=" ")
    semester = models.IntegerField(null=True,blank=True)
    roll_no = models.IntegerField(null=True,blank=True)
    id1 = models.FileField(upload_to='Rangoli/')
    def __str__(self):
        return self.name+" "+self.college_school

