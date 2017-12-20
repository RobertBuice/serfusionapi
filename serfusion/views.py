# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from api.models import Person


def home(request):
    return HttpResponse(status=200)
