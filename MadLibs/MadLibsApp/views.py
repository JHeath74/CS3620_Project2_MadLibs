import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import MadLibsStorage, MadLibsUserInput
from .forms import MadLibsUserInputForm


# Create your views here.

def index(request):
    template = loader.get_template("MadLibs/index.html")
    return HttpResponse(template.render())


def madlibuserinput(request):
    form = MadLibsUserInputForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('MadLibsApp:index')

    return render(request, 'MadLibs/madlibinput.html', {'form': form})


def madlibsdisplay(request):
    madlibs = MadLibsUserInput.objects.all().last()
    context = {
        'madlibs': madlibs
    }
    randomMadLib = [
        'Madlibs/MadLibsUserDisplay/madlibsdisplay.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay2.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay3.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay4.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay5.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay6.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay7.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay8.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay9.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay10.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay11.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay12.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay13.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay14.html',
        'Madlibs/MadLibsUserDisplay/madlibsdisplay15.html',

    ]
    pickRandomMadLib = random.choice(randomMadLib)
    return render(request, pickRandomMadLib, context)
