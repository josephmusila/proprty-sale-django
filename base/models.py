
from django.db import models

# Create your models here.



#define wether property is rental or for sale
class OwnershipStatus(models.Model):
    status=models.CharField(max_length=200)
   
    def __str__(self):
        return self.status

# define whether property is resident or commercial

class PropertyUsage(models.Model):
    propertyType=models.CharField(max_length=200)

    def __str__(self):
        return self.propertyType

#property owner

class Owner(models.Model):
    phoneContacts=models.CharField(max_length=200)
    ownerEmail=models.EmailField()
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    idnumber=models.IntegerField()

    # class Meta:
    #     verbose_name_plural="Owners"

    def __str__(self):
        return self.firstname


#model for a single property
class SingleProperty(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=400)
    slug=models.SlugField(unique=True)
    area=models.CharField(max_length=200)
    starting_price=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images")
    location=models.TextField(max_length=200)
    propertyType=models.ManyToManyField(PropertyUsage,blank=False,null=False)
    propertyStatus=models.ForeignKey(OwnershipStatus,on_delete=models.CASCADE)
    propertyInfrastructure=models.TextField(max_length=300)
    propertyAmenities=models.TextField(max_length=400)
    siteVisitDays=models.CharField(max_length=10)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    howToBuy=models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.name} - { self.location}'


