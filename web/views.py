from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.
from django.http import HttpResponse


class WebIndexView(View):
    
    def get(self, request, *args, **kwargs):
        """To get Website."""
        family_members = FamilyMember.objects.all()
        context = {'family_members': family_members}
        return render(request, 'web/index.html', context)