import re
from django.shortcuts import render
from django.http import HttpResponse

from . import util
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, title):
    if title in util.list_entries():
        content = markdown(util.get_entry(title))
        return render(request, 'encyclopedia/entry.html', {
            'title': title,
            'content': content
        })
    else:
        return render(request, 'encyclopedia/notfound.html')


def new(request):
    pass


def edit(request):
    pass


def random(request):
    pass


def search(request):
    pass
