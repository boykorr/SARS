from django.db.models import query
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

from SARS.models import Query, UserProfile
from SARS.forms import UserForm, UserProfileForm, QueryForm
from SARS_project.settings import BASE_DIR

import os
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
global relevanceList
relevanceList = {}

path = os.path.join(BASE_DIR, 'userQueries')

# the API we are using
# base URL used to open queries, only the abstract's ID should be appended
baseURL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
abstractURL = baseURL+"efetch.fcgi?db=pubmed&retmode=text&rettype=abstract&id="
# downloadURL = "esummary.fcgi?db=pubmed&id="


# getting the queries into a dictionary as long as sth has been typed
def query_construction(request):
    form = QueryForm()
    getQueryRequest = request.POST.get('queryBox')

    if (getQueryRequest is not "") and (getQueryRequest is not None) and (getQueryRequest not in printQuery):
        printQuery.append(str(getQueryRequest))
    context_dict = {'form': form, 'query': printQuery}

    # creates a document after an user where the queries that user has typed
    if request.user.is_authenticated():
        username = request.user.get_username()

        #file = os.path.join(path, username + ".txt")
        #queryFile = open(file,"w")
        #queryFile.write("Queries:\n")
        #queryFile.write(str(printQuery) + "\n")
        #queryFile.close

    else:
        del printQuery[:]

    del abstractList[:]
    return render(request, 'SARS/query_construction.html', context_dict)


def abstract_evaluation(request):
    printQuery[:]
    print "1"
    x = request.GET.getlist('data[]')
    for i in range(0, len(x), 1):
        print x[i]
        printQuery.append(x[i])
    print "2"
    print printQuery

    if x is not 0:
        if len(abstractList) is 0:
            searchURL = baseURL + "esearch.fcgi?db=pubmed&retmode=json&retmax=1&term=" + printQuery[0]
            for i in range(1, len(printQuery)):searchURL = searchURL + "+AND+" + x[i]

            print searchURL
            #webbrowser.open_new_tab(searchURL)

            wResp = urllib2.urlopen(searchURL)
            web_pg = wResp.read()
            #print web_pg

            splitData = web_pg.split()

            docNumber = splitData[11][1:-2]
            print docNumber

            global listID
            listID = (splitData[18:(splitData.index("],"))])

            n = len(listID)
            for i in range(0, n):
                if i < n-1:
                    listID[i] = listID[i][1:-2]
                else:
                    listID[i] = listID[i][1:-1]
                    
            for i in listID:print i

            print "3"
            
            for i in listID:
                #relevanceList[str(i)] = 0
                #print "4"

                searchURL = abstractURL + i
                print "5"

                wResp = urllib2.urlopen(searchURL)
                print "6"

                web_pg = wResp.read()[3:]
                print "7"

                abstractList.append(str(web_pg))
                print "8"

    print "9"
    #context_dict = {'docID': relevanceList.keys(), 'abstracts': abstractList}
    context_dict = {'abstracts': abstractList}

    print "10"
    return render(request, 'SARS/abstract_evaluation.html', context_dict)


def document_evaluation(request):
    context_dict = {'documentID': listID}
    return render(request, 'SARS/document_evaluation.html', context_dict)


def successful_registration(request):
    username = request.user.get_username()

    file = os.path.join(path, username + ".txt")
    queryFile = open(file, "w")
    queryFile.close()

    return HttpResponseRedirect('/SARS/')
