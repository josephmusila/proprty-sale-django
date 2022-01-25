from django.shortcuts import render
from django.template import context
from .models import SingleProperty,Owner,OwnershipStatus
from django.db.models import Q
# Create your views here.

def index(request):
    # singleproperty=SingleProperty.objects.all()
    
    q=request.GET.get('q') if request.GET.get('q') !=None else ''

    singleproperty=SingleProperty.objects.filter(
        Q(location__icontains=q)|
        Q(name__icontains=q)|
        Q(propertyInfrastructure__icontains=q)|
        Q(propertyAmenities__icontains=q)|
        Q(propertyStatus__status__icontains=q)
        
    )
    propertyCount=singleproperty.count()
    owner=Owner.objects.all()
    ownershipStatus=OwnershipStatus.objects.all()

    context={
        "allproperties":singleproperty,
        "propertyCount":propertyCount,
        "query":q,
        "owner":owner,
        "ownershipStatus":ownershipStatus
    }
    return render(request,"base/home.html",context)


def details(request,pk):
    singleproperty=None
    singleproperty=SingleProperty.objects.get(id=pk)
    context={
        "roomdetails":singleproperty
    }
    return render(request,"base/details.html",context)