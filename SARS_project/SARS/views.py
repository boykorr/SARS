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

printQuery = []

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
    #if request.session.test_cookie_worked():
        #print ">>>> TEST COOKIE WORKED!"
        #request.session.delete_test_cookie()
        #print request.COOKIES



    path = 'H:\Github\SARS\SARS_project\userQueries'
    currentUsername = User.objects.all().values_list('username')[len(User.objects.all().values_list('username'))-1][0] + ".txt"
    file = os.path.join(path, currentUsername)
    queryFile = open(file,"w")
    #userForm = QueryForm()
    #print userForm.fields['user']
    #print userForm.user.get_username()
    #response.set_cookie('yer_maw', datetime.now())
    #print request.COOKIES

    return HttpResponseRedirect('/SARS/')

