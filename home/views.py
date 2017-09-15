from django.shortcuts import render
from home.models import *
# Create your views here.
def index(request):
    cateparent = Category.objects.filter(cate_parent_id=0)
    storage = Product.objects.filter(product_status=1)
    context = {
        'parents' : cateparent,
        'featureItems' : storage
    }
    return render(request,"home/index.html", context)

def notfound(request):
    return render(request,'home/404.html')

def contact(request):
    return render(request,'home/contact.html')
