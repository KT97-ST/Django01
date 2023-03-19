from django.shortcuts import render, get_list_or_404

from .models import Question


# Create your views here.
def index(request):
    myname = "kimthanh"
    taisan = ["dien thoai", "may tinh", "may bay", "nhieu tien"]
    context = {"name": myname, "taisan": taisan}

    return render(request, "app01/index.html", context)


def viewlistquestion(request):
    list_question = get_list_or_404(Question, pk=1)
    context = {"list_question": list_question}
    return render(request, "app01/question_list.html", context)
