from django.db import models


# Create your models here.

class Resume(models.Model):
    resume_heading = models.CharField(
        "Resume heading",
        blank=False,
        null=False,
        default = "RESUME",
        max_length = 50,        
    )
    short_des = models.CharField(
        "Resume Short Description",
        max_length = 255
    )
    name = models.CharField(
        "Name",
        blank=False,
        null=False,
        max_length = 255        
    )
    summary = models.CharField(
        "Summary",
        max_length = 255       
    )
    address = models.CharField(
        "Address",
        blank=False,
        null=False,
        max_length = 255  
    )
    phone =models.IntegerField(
        "Phone Number",
        blank=False,
        null=False,
        max_length = 10          
    )
    email = models.EmailField(
        "Email",
        blank=False,
        null=False,        
    )

class Education(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    degree = models.CharField(
        "Degree",
        max_length = 100
    )
    institution = models.CharField(
        "Institution",
        max_length = 255
    )
    year_start = models.DateField(
        "Start Year"
    )
    year_end = models.DateField(
        "End Year",
        blank=True,
        null=True,       
    )
    description = models.TextField(
        "Description",
        blank=True,
        null=True,        
    )
    def __str__(self):
        return self.degree
class Award(models.Model):
    name = models.CharField("Award Name", max_length=255)
    description = models.TextField("Description", blank=True, null=True)

    def __str__(self):
        return self.name 
class Experience(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    title = models.CharField(
        "Profession Title",
        blank=False,
        null=False,
        max_length = 100
    )    
    company = models.CharField(
        "Company Name",
        blank=False,
        null=False,
        max_length = 255
    )
    location = models.CharField(
        "Company Location",
        blank=False,
        null=False,
        max_length = 255
    )
    year_start = models.DateField(
        "Start Year",
        blank=False,
        null=False,
    )
    year_end = models.DateField(
        "End Year",
        blank=True,
        null=True,       
    )
    description = models.TextField(
        "Description",
        blank=True,
        null=True,        
    )
    awards = models.ManyToManyField(
        Award, 
        blank=True
        )
    def __str__(self):
        return self.title
class Testimonials(models.Model):
    name = models.CharField(
        "Name",
        blank=False,
        max_length = 25
    )
    designation = models.CharField(
        "Designation",
        blank=False,
        max_length = 100        
    )
    quotes = models.CharField(
        "Quotes",
        blank=False,
        max_length =255
    )
    testimonials_img = models.ImageField(
        "Testimonials Image",
        upload_to="testimonials/",
        blank=False,
        null=False
    
    )
    def __str__(self):
        return self.name
    
class ContactDetails(models.Model):
    location = models.CharField(
        "Location",
        blank =False,
        max_length =100
    )
    email = models.EmailField(
        "Email",
        blank=False
    )
    phone = models.IntegerField(
        "Phone",
        blank=False
    )

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject