from django.http import HttpResponse
from django.shortcuts import render


content = 'Some content'


def index(request):
    # return HttpResponse('main page')
    title = 'Main page'
    return render(request, 'joke/index.html', {'title': title, 'content': content})


def randomjoke(request, jokeid):
    # return HttpResponse(f'<h1>Joke id: {jokeid}</h1>')
    title = 'Joke page'
    return render(request, 'joke/random_joke.html', {'title': title, 'content': content, 'jokeid': jokeid})
