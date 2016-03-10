from django.db.models import query
from django.shortcuts import render
from SARS.models import Query
from SARS.forms import UserForm, UserProfileForm, QueryForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def query_construction(request):
    form = QueryForm()
    return render(request, 'SARS/query_construction.html',{'form':form})

def abstract_evaluation(request):
    printQuery = request.POST.get('query')
    return HttpResponse(printQuery)

def successful_registration(request):
    return HttpResponseRedirect('/SARS/')