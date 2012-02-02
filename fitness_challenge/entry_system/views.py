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


def drawing(request):
    return render_to_response("fitness_challenge/drawing.html", context_instance=RequestContext(request))


def pick_winner(request):
    entries = WorkoutEntry.objects.all()

    random.seed()
    winner = random.randint(0, len(entries) - 1)

    return HttpResponseRedirect(reverse('entry_system.views.winner', args=(entries[winner].id,)))


def winner(request, entry_id):
    entry = WorkoutEntry.objects.get(id=entry_id)
    entries = WorkoutEntry.objects.all()
    half_entry_size = len(entries) / 2
    arc = math.pi / half_entry_size

    arcd = arc * 180 / math.pi
    spinTimeTotal = random.randint(0, 3) + 4 * 1000
    spinAngleStart = random.randint(0, 10) + 10
    startAngle = _rotateWheel(0, spinTimeTotal, spinAngleStart, 0)
    degrees = startAngle * 180 / math.pi + 90
    winner = int(math.floor((360 - degrees % 360) / arcd))

    template_variables = {'winner': entries[winner],
                          'entries': entries,
                          'entries_size': len(entries),
                          'arc': arc,
                          'spin_time_total': spinTimeTotal,
                          'spin_angle_start': spinAngleStart}
    return render_to_response("fitness_challenge/winner.html", template_variables,
                              context_instance=RequestContext(request))

def _rotateWheel(spinTime, spinTimeTotal, spinAngleStart, startAngle):
    spTime = spinTime + 30
    if (spinTime >= spinTimeTotal):
        return startAngle

    spinAngle = spinAngleStart - _easeOut(spTime, 0, spinAngleStart, spinTimeTotal);
    return _rotateWheel(spTime, spinTimeTotal, spinAngleStart, startAngle + (spinAngle * math.pi / 180))


def _easeOut(t, b, c, d):
    td = t / d
    ts = td *t
    tc = ts * t
    return b + c * (tc + -3 * ts + 3 * t)
