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

import urllib
import urllib2
import re
import webbrowser

global printQuery
printQuery = []
global username
username = None
global abstractList
abstractList = []

baseURL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
abstractURL = baseURL+"eutils/efetch.fcgi?db=pubmed&retmode=text&rettype=abstract&id="
# downloadURL = "esummary.fcgi?db=pubmed&id="

path = os.path.join(BASE_DIR, 'userQueries')


def query_construction(request):
    form = QueryForm()
    getQueryRequest = request.POST.get('queryBox')

    if getQueryRequest != "" and getQueryRequest != None and getQueryRequest not in printQuery:
        printQuery.append(str(getQueryRequest))
    context_dict = {'form': form, 'query': printQuery}

    if request.user.is_authenticated():
        username = request.user.get_username()

        file = os.path.join(path, username + ".txt")

        queryFile = open(file,"w")
        queryFile.write("Queries:\n")
        queryFile.write(str(printQuery) + "\n")
        queryFile.close

    return render(request, 'SARS/query_construction.html', context_dict)


def clear_all(request):
    del printQuery [:]
    return HttpResponseRedirect('/SARS')


def abstract_evaluation(request):
    if (printQuery):
        searchURL = baseURL + "esearch.fcgi?db=pubmed&retmode=json&retmax=20&term=" + printQuery[0]
        for i in range(1, len(printQuery)):searchURL = searchURL + "+AND+" + printQuery[i]
        # &usehistory=y Stores query in pubmed history server

        webbrowser.open_new_tab(searchURL)

        wResp = urllib2.urlopen(searchURL)
        web_pg = wResp.read()
        #print web_pg

        splitData = web_pg.split()
        docNumber = splitData[11][1:-2]
        print docNumber

        global finalData

        finalData = splitData[18:(splitData.index("],"))]

        for i in range(0, len(finalData)):finalData[i] = finalData[i][1:-1]
        for i in range(0, len(finalData)-1):finalData[i] = finalData[i][:-1]

        for n in finalData:print n

        for i in finalData:
            searchURL = abstractURL + i
            #print searchURL
            #webbrowser.open_new_tab(searchURL)
            wResp = urllib2.urlopen(searchURL)
            web_pg = wResp.read()
            abstractList.append(str(web_pg[3:]))

        context_dict = {'abstracts': abstractList}
        return render(request, 'SARS/abstract_evaluation.html', context_dict)


def document_evaluation(request):
    print finalData
    context_dict = {'documentID': finalData}
    return render(request, 'SARS/document_evaluation.html', context_dict)


def successful_registration(request):
    if request.user.is_authenticated():
        username = request.user.get_username()

    file = os.path.join(path, username + ".txt")
    queryFile = open(file, "w")
    queryFile.close()

    return HttpResponseRedirect('/SARS/')
