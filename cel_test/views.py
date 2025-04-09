from django.shortcuts import render
from .tasks import add

def celery_test(request, par1, par2):
    try:
        add.delay(par1,par2)
    except Exception as e:
        print(e)

def git_tag_test(request):
    return