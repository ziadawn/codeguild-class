'''
render is for a template
httpResponse is a quick way to get something on teh screen, not used much otherwise
httpResponseRedirect is when we want view to redirect to another page.
    Generally this is b/c the page does something with the database but not display something, so we send it to another view for user
reverse is for looking up a url so you don't have to hardcode it. What has it been named in your code rather than the absolute path?
'''

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Shorturl    # this is so we can write our function

import random

# Create your views here.

def index(request):
    # return HttpResponse('it works')     # filler text so we know things are working
    return render(request, 'shorturl/index.html', {})   # render takes in request, name of template, and context dictionary

# new view for saving data from template to model -- saveurl


def longurl(request):       # request is only for functions that are viewed by the user
    url = request.POST['text']      # this string needs to match name of input in index/template

    if url != "":
        shorturl = Shorturl(longurl=url, shorty=generate_shorty())  # here's my random shortener function
        shorturl.save()  # this saves to db
        return HttpResponse('http://localhost:8000/shorturl/' + shorturl.shorty)

    return HttpResponseRedirect(reverse('shorturl:index'))



def generate_shorty():      # don't need a thing in the parens here cuase this is a backend function
    urlsource = 'ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyz0123456789'
    i = 0
    shorty = ''
    while i < 9:
        shorty += random.choice(urlsource)
        i += 1
    return shorty


def redirect(request, code):        # code is a second paramenter, taken from urls
    randomshortvariable = get_object_or_404(Shorturl, shorty=code)      # in parens: looking in Shorturl table for a row whose value in column shorty is code
    url = randomshortvariable.longurl
    return HttpResponseRedirect('http://' + url)

