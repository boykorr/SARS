from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from SARS.models import Query, UserProfile
from SARS.forms import UserForm, UserProfileForm, QueryForm
from SARS_project.settings import BASE_DIR

import os
import urllib2

global printQuery
printQuery = []
global listID
listID = []
global documentDict
documentDict = []
global documentPool
documentPool = []
global documentResults
documentResults = []
global docNumber
docNumber = 0
global finalDocNumber
finalDocNumber = 0

path = os.path.join(BASE_DIR, 'userQueries')

# the API we are using
# base URL used to open queries, only the abstract's ID should be appended
baseURL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
abstractURL = baseURL+"efetch.fcgi?db=pubmed&retmode=text&rettype=abstract&id="
# downloadURL = "esummary.fcgi?db=pubmed&id="


def index(request):
    context_dict = {}
    return render(request, 'SARS/index.html', context_dict)


# getting the queries into a dictionary as long as sth has been typed
def basic_query(request):
    form = QueryForm()
    getQueryRequest = request.POST.get('queryBox')

    if (getQueryRequest is not "") and (getQueryRequest is not None) and (getQueryRequest not in printQuery):
        printQuery.append(str(getQueryRequest))
    context_dict = {'form': form, 'query': printQuery}

    # creates a document after an user where the queries that user has typed
    if request.user.is_authenticated():
        username = request.user.get_username()

    else:
        del printQuery[:]

    return render(request, 'SARS/basic_search.html', context_dict)


def advanced_query(request):
    return render(request, 'SARS/advanced_search.html')


def abstract_evaluation(request):
    if request.method == 'POST':
        del listID[:]
        del documentDict[:]

        quantity = request.POST.get('quantity')
        searchURL = baseURL + "esearch.fcgi?db=pubmed&retmode=json&retmax=" + quantity + "&term="

        if 'basic' in request.POST:
            print "basic"

            qString = request.POST.get('queryBox')
            qString = qString.split()
            print qString

            for s in qString: searchURL += s + "+"
            print searchURL

        else:
            print "advanced"
            qString = request.POST.get("the_docs")
            print qString
            searchURL += qString
            print searchURL

        wResp = urllib2.urlopen(searchURL)
        web_pg = wResp.read()
        splitData = web_pg.split()

        global docNumber
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

        for docID in listID:
            print docID
            searchURL = abstractURL + str(docID)
            wResp = urllib2.urlopen(searchURL)
            web_pg = wResp.read()[4:]

            splitData = web_pg.split("\n")
            title = ""
            for i in range(0, len(splitData)):
                if splitData[i] is "":
                    for j in range(i+1, len(splitData)):
                        if (splitData[j]!=""):
                            title += splitData[j] + " "
                        else:
                            break
                    break
            print title
            documentDict.append({"id": docID, "title": title, "summary": str(web_pg)})
    else:
        print "not a post request"

    context_dict = {'docCount': docNumber, 'abstracts': documentDict}
    return render(request, 'SARS/abstract_evaluation.html', context_dict)


def document_evaluation(request):
    if request.method == 'POST':
        print "DOCUMENT POST"

        data = request.POST.get('the_docs')
        data = data.split("/")
        data = data[:-1]

        if data[0] == "R":
            print "REFRESH TOKEN"

            del documentPool[:]

            global docNumber
            docNumber = len(data) - 1
            print docNumber

            for docID in data:
                for doc in documentDict:
                    if docID == doc["id"]:
                        documentPool.append({
                            "id": docID,
                            "title": doc["title"],
                            "url": "https://www.ncbi.nlm.nih.gov/pubmed/" + str(docID)
                        })
                        break

    elif request.method == 'GET':
        print "GET"

    context_dict = {'docCount': docNumber, 'documents': documentPool}
    return render(request, 'SARS/document_evaluation.html', context_dict)


def document_results(request):
    print "document results"
    if request.method == 'POST':
        del documentResults[:]

        print "RESULTS POST"
        data = request.POST.get('the_docs')
        print data

        data = data.split("/")
        data = data[:-1]
        print data

        global finalDocNumber
        finalDocNumber = len(data)
        print finalDocNumber

        for docID in data:
            for doc in documentPool:
                if docID == doc["id"]:
                    documentResults.append(doc)
                    break

    else:
        print "GET"

    context_dict = {'docCount': finalDocNumber, 'results': documentResults}
    return render(request, 'SARS/document_results.html', context_dict)


def successful_registration(request):
    username = request.user.get_username()

    file = os.path.join(path, username + ".txt")
    queryFile = open(file, "w")
    queryFile.close()

    return HttpResponseRedirect('/SARS/')


def user_guide(request):
    return render(request, 'SARS/user_guide.html')
