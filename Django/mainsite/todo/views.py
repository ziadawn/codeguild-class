# from django.shortcuts import render

# Create your views here.

# could write all your html here in view!! whaaaat. See example under def index below

# SEPARATION OF CONCERNS. IN INDEX PUT THE CODE TO

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import TodoItem                # the . is the current working directory

def index(request):

    # output = '<html><head></head><body>'
    # output += '<ul>'  # this is an unordered list
    # for i in range(100):
        # output += f'<li>{i}</li>'
    # output += '</body></html>'
    # print(output)
    # return HttpResponse('Hello World!')

    # todo_items = TodoItem.objects.all()
    #
    # # print(todo_items)       # this prints in the terminal, NOT the browser
    #
    # output = '<html><head></head><body>'
    # output += '<ul>'
    #
    # for todo_item in todo_items:
    #     # print(todo_item.todo_text)          # todo_text is the variable from models.py
    #     output += f'<li>{todo_item.todo_text}</li>'
    # output += '</ul>'
    # output += '</body></html>'
    # # return HttpResponse('Tea!! More tea!')
    # return HttpResponse(output)
    #
    #
    # context = {'number': 27}              # this is linked from the index.html file

    todo_items = TodoItem.objects.all()     # this is linked from the index.html file

    context = {'todo_items': todo_items}
    return render(request, 'todo/index.html', context)


def savetodo(request):

    todo_text = request.POST['text']

    todo_item = TodoItem(todo_text=todo_text)   # (name, value) just named the same thing
    todo_item.save()

    return HttpResponseRedirect(reverse('todo:index'))


