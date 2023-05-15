from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Index(TemplateView):
    template_name = 'chess/index.html'

class Feedback(TemplateView):
    template_name = 'chess/feedback.html'

class About(TemplateView):
    template_name = 'chess/about.html'
