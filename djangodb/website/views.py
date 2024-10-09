from django.shortcuts import render
from .models import member

# Create your views here.
def home(request):
    all_members = member.objects.all

    return render(request, 'home.html', {'all':all_members})



def join(request):
    return render(request, 'join.html', {})