"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    context = {}
    context['title'] = 'SF Movie Map'
    context['year'] = datetime.now().year
    return render(
        request,
        'app/index.html',
        context)

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    context = {}
    context['title'] = 'Contact'
    context['message'] = 'Your contact page.'
    context['year'] = datetime.now().year
    return render(
        request,
        'app/contact.html',
        context)

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    context['title'] = 'About'
    context['message'] = 'SF Movie Map.'
    context['year'] = datetime.now().year
    return render(
        request,
        'app/about.html',
        context)
