from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from fitness_challenge.entry_system.models import WorkoutEntry

def entry(request):
    return render_to_response("entry/entry.html", context_instance=RequestContext(request))


def process(request):
    print(request.POST)
    entry = WorkoutEntry(name=request.POST['name'], date=request.POST['date'])
    entry.save()
    return HttpResponseRedirect(reverse('entry_system.views.entry'))
