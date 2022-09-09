class Mechrelay(models.Model):
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
    id1 = models.FileField(upload_to='Mechrelay/')
    def _str_(self):
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
    def _str_(self):
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
    def _str_(self):
        return self.name+" "+self.college_school
class Surveyscout(models.Model):
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
    id1 = models.FileField(upload_to='Surveyscout/')
    def _str_(self):
        return self.name+" "+self.college_school

class TechnicalquizCe(models.Model):
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
    id1 = models.FileField(upload_to='TechnicalquizCe/')
    def _str_(self):
        return self.name+" "+self.college_school
