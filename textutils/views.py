# Created by ANX
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #params = {'name':'Anshul','place':'Nagpur'}
    return render(request, 'index.html')
    #return HttpResponse("Home")


def analyze(request):
    djtext = request.GET.get('text', 'default')                 # Getting Text from TEXTAREA
    removepunc = request.GET.get('removepunc', 'default')       # Check Box Value
    fullcaps = request.GET.get('fullcaps', 'default')
    newlineremover = request.GET.get('newlineremover', 'default')
    spaceremover = request.GET.get('spaceremover', 'default')
    charcount = request.GET.get('charcount', 'default')
    # print(djtext)
    # print(removepunc)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc == 'on':
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to UpperCase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char !='\n':
                analyzed = analyzed + char
        params = {'purpose': 'Remove new Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcount == 'on':
        analyzed = len(djtext)
        params = {'purpose': 'Total Char', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("error")

