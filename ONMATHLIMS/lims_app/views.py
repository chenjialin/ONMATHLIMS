# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from forms import SampleProjectMasterForm
from django.core.urlresolvers import reverse
from django.shortcuts import render
import os
# Create your views here.
CODE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def welcome(request):
    return HttpResponse("<h1>Welcome to my tiny twitter!</h1>")


def project_input(request):
    if request.method == "POST":
        form = SampleProjectMasterForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.save()
            return HttpResponseRedirect(reverse("welcome"))
    else:
        form = SampleProjectMasterForm()
    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'project_input.html'), {'form': form})


def main(request):
    username = "陈中旭"
    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'index.html'),
                  {'username': username})


def receive_sample(request):
    username = "陈中旭"
    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'receive_sample.html'),
                  {'username': username})