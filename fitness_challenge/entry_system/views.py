from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from fitness_challenge.entry_system.models import WorkoutEntry

def entry(request):
    return render_to_response("entry/entry.html", context_instance=RequestContext(request))


def process(request):
    entry = WorkoutEntry(name=request.POST['name'], date=request.POST['date'])
    entry.save()
    return HttpResponseRedirect(reverse('entry_system.views.entry'))


def drawing(request):
    return render_to_response("entry/drawing.html", context_instance=RequestContext(request))


def pick_winner(request):
    entries = WorkoutEntry.objects.all()

    return HttpResponseRedirect(reverse('entry_system.views.winner', args=(entries[2].id,)))


def winner(request, entry_id):
    entry = WorkoutEntry.objects.get(id=entry_id)

    return render_to_response("entry/winner.html", {'entry': entry})
