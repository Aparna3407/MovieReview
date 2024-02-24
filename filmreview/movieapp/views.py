from django.shortcuts import render, redirect
from . models import Movie
from . models import Review
from . forms import ReviewForm




def add_movie(request):
    if request.method=="POST":
        title=request.POST.get('title')
        description = request.POST.get('description')
        title_upload_date = request.POST.get('title_upload_date')
        movie_cover = request.FILES['movie_cover']
        movie=Movie(title=title,description=description,title_upload_date=title_upload_date,movie_cover=movie_cover)
        movie.save()
    return render(request,'add.html')

def rate(request, id):
    post = Movie.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        author = request.POST.get('author')
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(author=author, stars = stars,  comment=comment , movie=post)
        review.save()
        return redirect('/')

    form = ReviewForm()
    context = {
        "form":form

    }
    return render(request, 'rate.html',context)

def about(request):
    return render(request,'about.html')
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=ReviewForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

