from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import PostForm, SendEmail


# Create your views here.
class IndexClass(View):
    def get(self, request):
        ketqua = "123456"
        return HttpResponse(ketqua)

class ClassSaveNews(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'news/add_new.html', {'form': form})
    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("luu thanh cong")
        else:
            return HttpResponse("khong duoc validate")



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
