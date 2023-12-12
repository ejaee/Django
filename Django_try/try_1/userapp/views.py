from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.

from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from rest_framework.views import APIView
from .serializers import UserSerializer
class UserListAPI(APIView):
    def get(self, request):
        queryset = User.objects.all()
        print(queryset)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


def index(request):
    # 2
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # 3
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("userapp/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 4
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "userapp/index.html", context)

def detail(request, question_id):
    # 1
    # return HttpResponse("You're looking at question %s." % question_id)

    # 2
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "userapp/detail.html", {"question": question})

    # 3
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "userapp/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)