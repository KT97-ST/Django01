from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm


# Create your views here.
def index(request):
    return HttpResponse("chao")


def add_post(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("luu thanh cong")
        else:
            return HttpResponse("khong duoc validate")
    else:
        form = PostForm()
        return render(request, 'news/add_new.html', {'f': form})
