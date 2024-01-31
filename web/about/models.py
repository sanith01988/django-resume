from django.db import models

# Create your models here.
class About(models.Model):
    heading = models.TextField(
        "About Heading",
        blank=False,
        null=False
    )
    title = models.CharField(
        "About Title",
        max_length=255,
        blank=False,
        null=False
    )
    summary = models.CharField(
        "Short Summury",
        max_length=255,
        blank=False,
        null=False
    )
    about_img = models.ImageField(
        "About Image",
        upload_to="about/",
        blank=False,
        null=False
    
    )
    dob = models.DateField(
        verbose_name="Date of Birthday"
    )
    website = models.CharField(
        "Website URL",
        max_length=255
    )
    phone = models.BigIntegerField(default=0)
    city = models.CharField(
        "City",
        max_length=255
    )
    age = models.IntegerField(
        "Age",
        default=0
    )
    degree = models.CharField(
        "Degree",
        max_length =255
    )
    email = models.EmailField(
        "Email Address"
    )
    freelance = models.BooleanField(
        "Freelancing",
        default=False
    )
    
    def __str__(self, *args, **kwargs):
        return f'{self.id} {self.title}'
    
    def __unicode__(self,*args,**kwargs):
        return f'{self.id} {self.title}'
    