from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from .forms import movie_form
from . models import movie


def index(request):
    moives=movie.objects.all()
    context={'movie_list':moives}
    return render(request,'index.html',context)

# def detail(request,movieid):
#     movie_li= movie.objects.get(id=movieid)
#     list=movie.objects.all()
#     return render(request,'movie_details.html',{'movie':movie_li,'m_list':list})
def detail(request,movieid):
    movies=movie.objects.get(id=movieid)
    context={'products':movies}

    return render(request,"movie_details.html",context)
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year = request.POST.get('year')
        img=request.FILES.get('img')
        add_data=movie(name=name,desc=desc,year=year,image=img)
        add_data.save()
        return redirect('/')
    return  render(request,'add_movie.html')

def update(request,movieid):
    movie_up=movie.objects.get(id=movieid)
    context = {'products': movie_up}
    form_up=movie_form(request.POST or None,request.FILES,instance=movie_up)
    if form_up.is_valid():
        form_up.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form_up,'products': movie_up})
def delete(request,movieid):
    if request.method=='POST':
        movie_del = movie.objects.get(id=movieid)
        movie_del.delete()
        return redirect('/')
    return render (request,'delete.html')