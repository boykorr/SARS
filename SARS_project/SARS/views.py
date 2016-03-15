from django.db.models import query
from django.shortcuts import render
from SARS.models import Query
from SARS.forms import UserForm, UserProfileForm, QueryForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import os

printQuery = []

def query_construction(request):
    form = QueryForm()
    global printQuery
    getQueryRequest = request.POST.get('queryBox')
    if getQueryRequest != "" and getQueryRequest != None and getQueryRequest not in printQuery:
        printQuery.append(str(getQueryRequest))
    context_dict = {'form':form, 'query':printQuery}
    return render(request, 'SARS/query_construction.html', context_dict)

def abstract_evaluation(request):
    printQuery = request.POST.get('queryBox')
    return HttpResponse(printQuery)

def successful_registration(request):

    path = 'H:\Github\SARS\SARS_project\userQueries'
    currentUsername = "bil.txt"
    file = os.path.join(path, currentUsername)
    queryFile = open(file,"w")

    return HttpResponseRedirect('/SARS/')

