from django.shortcuts import render
from .models import Books
from django.http import HttpResponse
from .models import Category

# Create your views here.

def index(request):
    # allbooks=Books.objects.all()
    # first=Books.objects.get(pk=1)
    # history=Books.objects.filter(category_id=2)
    # rebis= Books.objects.filter(publishingHouse_id=1)
    #
    # null=Books.objects.filter(category_id__isnull=True)
    # ijon=Books.objects.filter(description__icontains='Ijon Tichy')
    cateogries = Category.objects.all()
    data={'categories':cateogries}
    return render(request,'template.html',data)

def category(request,id):
    onecategory=Category.objects.get(pk=id)
    book_category=Books.objects.filter(category_id=onecategory)
    categories=Category.objects.all()
    data={'onecategory':onecategory,'book_category':book_category,'categories':categories}
    return render(request,'book_category.html',data)

def title(request,id):
    onetitle=Books.objects.get(pk=id)
    return HttpResponse(onetitle.name)

def book(request,id):
    onebook=Books.objects.get(pk=id)
    categories=Category.objects.all()
    data={'onebook':onebook,'categories':categories}
    return render(request,'book.html',data)
