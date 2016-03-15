from django.db.models import query
from django.shortcuts import render
from SARS.models import Query
from SARS.forms import UserForm, UserProfileForm, QueryForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

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
    return HttpResponseRedirect('/SARS/')