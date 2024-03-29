import email
from os import terminal_size
from typing import Collection

from django.db import models
from django.db.models.fields.files import FieldFile


# Create your models here.
INT_CHOICES = (
    ("college", "college"),
    ("school", "school"),
    
  
)

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
    email2 = models.EmailField( max_length=254,default="")
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='ProjectDisplay/',blank=True,null=True)

    name3 = models.CharField(max_length=20,default=" ")
    email3 = models.EmailField( max_length=254,default="")
    phone3 = models.CharField(default=" ",max_length=12)
    branch3 = models.CharField(max_length=50,default=" ")
    semester3 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno3 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id3 = models.FileField(upload_to ='ProjectDisplay/',blank=True,null=True)

    name4 = models.CharField(max_length=20,default=" ")
    email4 = models.EmailField( max_length=254,default="")
    phone4 = models.CharField(default=" ",max_length=12)
    branch4 = models.CharField(max_length=50,default=" ")
    semester4 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno4 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id4 = models.FileField(upload_to ='ProjectDisplay/',blank=True,null=True)

    name5 = models.CharField(max_length=20,default=" ")
    email5 = models.EmailField( max_length=254,default="")
    phone5 = models.CharField(default=" ",max_length=12)
    branch5 = models.CharField(max_length=50,default=" ")
    semester5 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno5 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id5 = models.FileField(upload_to ='ProjectDisplay/',blank=True,null=True)
    def __str__(self):
        return self.teamname + " " +self.college

class Robolympics(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    college = models.CharField(max_length=200,default="")
    teamname = models.CharField(max_length=200,default=" ")
    eventype = models.CharField(max_length=200,default="")
    
    name1 = models.CharField(max_length=20,default=" ")
    email1 = models.EmailField( max_length=254,default="")
    phone1 = models.CharField(max_length=12,default=" ")
    branch1 = models.CharField(max_length=50,default=" ")
    semester1 = models.CharField(null=True,blank=True,default=" ",max_length=3)
    rollno1 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id1 = models.FileField(upload_to ='Robolympics/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254,default="")
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='Robolympics/',blank=True,null=True)

    name3 = models.CharField(max_length=20,default=" ")
    email3 = models.EmailField( max_length=254,default="")
    phone3 = models.CharField(default=" ",max_length=12)
    branch3 = models.CharField(max_length=50,default=" ")
    semester3 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno3 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id3 = models.FileField(upload_to ='Robolympics/',blank=True,null=True)

    name4 = models.CharField(max_length=20,default=" ")
    email4 = models.EmailField( max_length=254,default="")
    phone4 = models.CharField(default=" ",max_length=12)
    branch4 = models.CharField(max_length=50,default=" ")
    semester4 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno4 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id4 = models.FileField(upload_to ='Robolympics/',blank=True,null=True)


    def __str__(self):
        return self.name1+" "+self.college


class Techcharades(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    teamname = models.CharField(max_length=50,default="")
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    branch_class = models.CharField(max_length=50,default=" ")
    semester = models.IntegerField(null=True,blank=True)
    roll_no = models.IntegerField(null=True,blank=True)
    id1 = models.FileField(upload_to='Techcharades/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254,default="")
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='Techcharades/',blank=True,null=True)

    def __str__(self):
        return self.name+" "+self.college_school

class TechnicalCollage(models.Model):
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
    id1 = models.FileField(upload_to ='TechnicalCollage/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254,default="")
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='TechnicalCollage/',blank=True,null=True)

    name3 = models.CharField(max_length=20,default=" ")
    email3 = models.EmailField( max_length=254,default="")
    phone3 = models.CharField(default=" ",max_length=12)
    branch3 = models.CharField(max_length=50,default=" ")
    semester3 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno3 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id3 = models.FileField(upload_to ='TechnicalCollage/',blank=True,null=True)
    
    def __str__(self):
        return self.name1+" "+self.college

class FloatingConcreteBoat(models.Model):
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
    id1 = models.FileField(upload_to ='FloatingConcreteBoat/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254,default="")
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='FloatingConcreteBoat/',blank=True,null=True)

    name3 = models.CharField(max_length=20,default=" ")
    email3 = models.EmailField( max_length=254,default="")
    phone3 = models.CharField(default=" ",max_length=12)
    branch3 = models.CharField(max_length=50,default=" ")
    semester3 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno3 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id3 = models.FileField(upload_to ='FloatingConcreteBoat/',blank=True,null=True)

    name4 = models.CharField(max_length=20,default=" ")
    email4 = models.EmailField( max_length=254,default="")
    phone4 = models.CharField(default=" ",max_length=12)
    branch4 = models.CharField(max_length=50,default=" ")
    semester4 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno4 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id4 = models.FileField(upload_to ='FloatingConcreteBoat/',blank=True,null=True)

    name5 = models.CharField(max_length=20,default=" ")
    email5 = models.EmailField( max_length=254,default="")
    phone5 = models.CharField(default=" ",max_length=12)
    branch5 = models.CharField(max_length=50,default=" ")
    semester5 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno5 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id5 = models.FileField(upload_to ='FloatingConcreteBoat/',blank=True,null=True)
    def __str__(self):
        return self.name1+" "+self.college
        
class Mechrelay(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    college = models.CharField(max_length=200,default="")
    teamname = models.CharField(max_length=200,default=" ")
    name1 = models.CharField(max_length=20,default=" ")
    email1 = models.EmailField( max_length=254,default="")
    phone1 = models.CharField(max_length=12,default=" ")
    branch1 = models.CharField(max_length=50,default=" ")
    semester1 = models.CharField(null=True,blank=True,default=" ",max_length=3)
    rollno1 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id1 = models.FileField(upload_to ='Mechrelay/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254,default="")
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='Mechrelay/',blank=True,null=True)

    name3 = models.CharField(max_length=20,default=" ")
    email3 = models.EmailField( max_length=254,default="")
    phone3 = models.CharField(default=" ",max_length=12)
    branch3 = models.CharField(max_length=50,default=" ")
    semester3 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno3 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id3 = models.FileField(upload_to ='Mechrelay/',blank=True,null=True)

    name4 = models.CharField(max_length=20,default=" ")
    email4 = models.EmailField( max_length=254,default="")
    phone4 = models.CharField(default=" ",max_length=12)
    branch4 = models.CharField(max_length=50,default=" ")
    semester4 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno4 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id4 = models.FileField(upload_to ='Mechrelay/',blank=True,null=True)

    def __str__(self):
        return self.teamname + " " +self.college


       
class Bplan(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    teamname = models.CharField(max_length=50,default="")
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    branch_class = models.CharField(max_length=50,default=" ")
    semester = models.IntegerField(null=True,blank=True)
    roll_no = models.IntegerField(null=True,blank=True)
    id1 = models.FileField(upload_to='Bplan/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254,default="")
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='Bplan/',blank=True,null=True)
    def __str__(self):
        return self.name+" "+self.college_school

class Groupdiscussion(models.Model):
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
    id1 = models.FileField(upload_to='Groupdiscussion/')
    def __str__(self):
        return self.name+" "+self.college_school

class Masterminds(models.Model):
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
    id1 = models.FileField(upload_to='Masterminds/')
    def __str__(self):
        return self.name+" "+self.college_school

class Surveyscout(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    college = models.CharField(max_length=200,default="")
    teamname = models.CharField(max_length=200,default=" ")
    projectname = models.CharField(max_length=100,default=" ")
    name1 = models.CharField(max_length=20,default=" ")
    email1 = models.EmailField( max_length=254,default="")
    phone1 = models.CharField(max_length=12,default=" ")
    branch1 = models.CharField(max_length=50,default=" ")
    semester1 = models.CharField(null=True,blank=True,default=" ",max_length=3)
    rollno1 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id1 = models.FileField(upload_to ='Surveyscout/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254,default="")
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='Surveyscout/',blank=True,null=True)

    name3 = models.CharField(max_length=20,default=" ")
    email3 = models.EmailField( max_length=254,default="")
    phone3 = models.CharField(default=" ",max_length=12)
    branch3 = models.CharField(max_length=50,default=" ")
    semester3 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno3 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id3 = models.FileField(upload_to ='Surveyscout/',blank=True,null=True)

    name4 = models.CharField(max_length=20,default=" ")
    email4 = models.EmailField( max_length=254,default="")
    phone4 = models.CharField(default=" ",max_length=12)
    branch4 = models.CharField(max_length=50,default=" ")
    semester4 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno4 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id4 = models.FileField(upload_to ='Surveyscout/',blank=True,null=True)

    name5 = models.CharField(max_length=20,default=" ")
    email5 = models.EmailField( max_length=254,default="")
    phone5 = models.CharField(default=" ",max_length=12)
    branch5 = models.CharField(max_length=50,default=" ")
    semester5 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno5 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id5 = models.FileField(upload_to ='Surveyscout/',blank=True,null=True)
    def __str__(self):
        return self.teamname + " " +self.college


class TechnicalquizCe(models.Model):
    type_institution  = models.CharField(
        max_length = 20,
        choices = INT_CHOICES,
        default = 'college'
        )
    teamname = models.CharField(max_length=50,default="")
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    college_school = models.CharField(max_length=200,default="")
    branch_class = models.CharField(max_length=50,default=" ")
    semester = models.IntegerField(null=True,blank=True)
    roll_no = models.IntegerField(null=True,blank=True)
    id1 = models.FileField(upload_to='TechnicalquizCe/')

    name2 = models.CharField(max_length=20,default=" ")
    email2 = models.EmailField( max_length=254,default="")
    phone2 = models.CharField(default=" ",max_length=12)
    branch2 = models.CharField(max_length=50,default=" ")
    semester2 = models.CharField(null=True,blank=True,default=" ",max_length=5)
    rollno2 = models.CharField(null=True,blank=True,default=" ",max_length=20)
    id2 = models.FileField(upload_to ='TechnicalquizCe/',blank=True,null=True)
    def __str__(self):
        return self.name+" "+self.college_school
