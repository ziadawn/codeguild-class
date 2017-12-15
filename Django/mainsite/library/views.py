
'''
render is for a template
httpResponse is a quick way to get something on the screen, not used much otherwise
httpResponseRedirect is when we want view to redirect to another page.
    Generally this is b/c the page does something with the database but not display something, so we send it to another view for user
reverse is for looking up a url so you don't have to hardcode it. What has it been named in your code rather than the absolute path?
'''

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Book, Author, Checkout    # this is so we can write our function



def index(request):
    books = Book.objects.all()                  # variable is list of all books in db. All the properties are now accessible
    context = {'books': books}                  # dictionary, where the value is the books we just pulled above
    return render(request, 'library/index.html', context)

    # return HttpResponse('library test!')     # filler text so we know things are working

    # create variable in index that pulls books from database and saves as variable
    # this variable will be put into dictionary format and passed to render and the context


def checkout(request):
    book = get_object_or_404(Book, pk=request.POST['book'])
    check = Checkout(book=book, checkout=request.POST['check'] == 'out', user=request.POST['user'])
    check.save()
    print(request.POST)
    return HttpResponseRedirect(reverse('library:index'))


def checkout_history(request):
    history = Checkout.objects.all()            # getting all the data from Checkout db, sending to dictionary below
    return render(request, 'library/checkout_history.html', {'history':history})    # sending that info to template

