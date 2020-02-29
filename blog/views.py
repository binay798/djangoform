from django.shortcuts import render,redirect
from .forms import *
from .forms import PostForm
# Create your views here.
def home(request):
    posts = Posts.objects.all()
    context = {'posts':posts}
    return render(request,'blog/index.html',context)
    

def add_post(request):


    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    else:
        form = PostForm(request.POST)
    context = {'form':form}
    return render(request,'blog/form.html',context)



