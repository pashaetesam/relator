from django.shortcuts import render

from listings.models import Listing

def index(request):
  listings = Listing.objects.all()
  print (listings)
  print ("paul is ther best")
  context = {
   'listings':listings
  }
    # context = {
    #   'name':'Pasha',
    #   'lastname':'Etesam'
    #   }
  print ("paul2 is ther best")

  return render(request,'listings/listings.html',context)

def listing(request):
  return render(request, 'listings/listing.html')

def search(request):
    return render(request,'listings/search.html') 


