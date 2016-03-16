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


global printQuery
printQuery = []
global username
username = None
global baseURL
baseURL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
#downloadURL = "esummary.fcgi?db=pubmed&id="

path = os.path.join(BASE_DIR,'userQueries')

def query_construction(request):
    form = QueryForm()
    getQueryRequest = request.POST.get('queryBox')

    if getQueryRequest != "" and getQueryRequest != None and getQueryRequest not in printQuery:
        printQuery.append(str(getQueryRequest))
    context_dict = {'form':form, 'query':printQuery}

    if request.user.is_authenticated():
        username = request.user.get_username()

        file = os.path.join(path, username + ".txt")
        queryFile = open(file,"w")
        queryFile.write("Queries:\n")

        #if len(printQuery) > 0 and printQuery[-1] != "" and printQuery[-1] != None:
        #    for query in printQuery:
        #        queryFile.write(query + "\n")

    return render(request, 'SARS/query_construction.html', context_dict)

def abstract_evaluation(request):

#open in a new tab

    searchURL = baseURL + "esearch.fcgi?db=pubmed&term=" + printQuery[0]
    for i in range(1, len(printQuery)):
        searchURL = searchURL + "+AND+" + printQuery[i]
        #&usehistory=y Stores query in pubmed history server
    webbrowser.open_new_tab(searchURL)

    return render(request, 'SARS/abstract_evaluation.html',{})


def successful_registration(request):
    if request.user.is_authenticated():
        username = request.user.get_username()

    file = os.path.join(path, username + ".txt")
    queryFile = open(file,"w")
    queryFile.close()

    return HttpResponseRedirect('/SARS/')
