from django.db.models import query
from django.shortcuts import render
from SARS.models import Query, UserProfile
from SARS.forms import UserForm, UserProfileForm, QueryForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import os
from django.contrib.auth.models import User
from datetime import datetime
from SARS_project.settings import BASE_DIR

printQuery = []
username = ''

def query_construction(request):
    form = QueryForm()
    global printQuery
    getQueryRequest = request.POST.get('queryBox')
    if getQueryRequest != "" and getQueryRequest != None and getQueryRequest not in printQuery:
        printQuery.append(str(getQueryRequest))
    context_dict = {'form':form, 'query':printQuery}
    #print User.objects.all().values_list('username')[len(User.objects.all().values_list('username'))-1][0]
    return render(request, 'SARS/query_construction.html', context_dict)

def abstract_evaluation(request):
    printQuery = request.POST.get('queryBox')
    return HttpResponse(printQuery)

def successful_registration(request):
    print request.POST
    path = os.path.join(BASE_DIR,'userQueries')
    global username
    username = User.objects.all().values_list('username')[len(User.objects.all().values_list('username'))-1][0]

    file = os.path.join(path, username + ".txt")
    queryFile = open(file,"w")

    return HttpResponseRedirect('/SARS/')

