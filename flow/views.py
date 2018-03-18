# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def Test(request):
    a = 'hello world!'
    return render(request,"flow/test.html",locals())