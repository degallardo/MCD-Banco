from django.http import HttpResponse
from django.db import connection


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    cursor = connection.cursor()
    cursor.execute('SELECT question_text FROM polls_question WHERE id = 1')
    row = cursor.fetchone()
    print(row)
    # return HttpResponse("You're voting on question %s." % question_id)
    return HttpResponse("You're voting on question %s." % row)