from django.http import HttpResponse
from django.shortcuts import render

from .forms import PostForm, SendEmail


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


def email_view(request):
    email = SendEmail()
    return render(request, 'news/email.html', {"email": email})


def process_email(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            title = m.cleaned_data['title']
            content = m.cleaned_data['content']
            cc = m.cleaned_data['cc']
            email = m.cleaned_data['email']
            context = {"title": title,
                      "content": content,
                      "cc": cc,
                      "email": email}
            return render(request, "news/print_email.html", context)
        else:
            return HttpResponse("from not validate")
    else:
        return HttpResponse("do not post method")
