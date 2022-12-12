
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.POST.get ('text', 'defult')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuation', 'analyzed_text': analyzed}
        text = analyzed

    if capitalize == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose':'capitalize', 'analyzed_text': analyzed}
        text = analyzed


    if(newLineRemover == "on"):
        analyzed = ""
        for char in text:
            if char != ("\n") and char != ("\r"):
                analyzed = analyzed + char
        params = {'purpose':'Remove New Line','analyzed_text':analyzed}
        text = analyzed


    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate (text):
            if not(text[index] == " " and text[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Remove Extra Spaces','analyzed_text': analyzed}


    if(removepunc!="on" and capitalize!="on" and newLineRemover!="on" and extraspaceremover!="on"):
        return HttpResponse("<h3> << Please Choose Any Option >> </h3>")

    return render (request, 'analyze.html', params)        
