from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Question


# Create your views here.
def index(request):
    myname = "kimthanh"
    taisan = ["dien thoai", "may tinh", "may bay", "nhieu tien"]
    context = {"name": myname, "taisan": taisan}

    return render(request, "app01/index.html", context)


def viewlistquestion(request):
    # list_question = get_list_or_404(Question, pk=1)
    list_question = Question.objects.all()
    context = {"list_question": list_question,
               "title": "Tra Loi Cau Hoi"}
    return render(request, "app01/question_list.html", context)


def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    context = {
        "qs": q,
        "name": "Chu tich",
        "questiontext": q.question_text,
        "title": "Tra Loi Cau Hoi"}
    return render(request, "app01/detail_question.html", context)

def choiceVote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        rq = request.POST["choice"]
        c = q.choice_set.get(pk=rq)
        c.vote = c.vote + 1
        c.save()
    except:
        HttpResponse("Khong tim thay doi tuong")
    return render(request, "app01/result.html", {"q":q})