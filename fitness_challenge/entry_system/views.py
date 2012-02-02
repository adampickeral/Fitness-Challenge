import random
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
import math
from fitness_challenge.entry_system.models import WorkoutEntry


def fitness_challenge(request):
    return render_to_response("fitness_challenge/index.html")


def entry(request):
    return render_to_response("fitness_challenge/entry.html", context_instance=RequestContext(request))


def process(request):
    entry = WorkoutEntry(name=request.POST['name'], date=request.POST['date'])
    entry.save()
    return HttpResponseRedirect(reverse('entry_system.views.fitness_challenge'))


def winner(request):
    entries = WorkoutEntry.objects.all()

    template_variables = {'entries': entries,
                          'entries_size': len(entries)
                         }
    return render_to_response("fitness_challenge/winner.html", template_variables,
                              context_instance=RequestContext(request))
