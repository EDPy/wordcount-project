from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.pyplot import plot
import pygal

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddict = {}
    for word in wordlist:
        if word in worddict:
            #increase value
            worddict[word] += 1
        else:
            #put word in the dictionarz
            worddict[word] = 1

    chart = pygal.Bar()
    chart.title = 'Most used words'


    #sorteddict = sorted(worddict.items(), key=worddict.items.lower, reverse=True)

    for word in worddict:
        chart.add(word, worddict[word])
    chart.render_to_file('barchart.svg')

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddict':worddict.items()})

def about(request):
    return render(request, 'about.html')