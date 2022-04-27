from django.shortcuts import redirect, render
from .forms import AddBlogForm
from .models import Blog
# Create your views here.


def index(request):
    blogForm = AddBlogForm()
    blogs  = Blog.objects.all()
    
    if request.method == 'POST':
        blogForm = AddBlogForm(request.POST)
        if blogForm.is_valid():
            blogForm.save()
            return redirect('/')
        else:
            blogForm = AddBlogForm(request.POST)

    context = {
        "blogForm": blogForm,
        "blogs": blogs,
    }
    return render(request, 'index.html', context)
