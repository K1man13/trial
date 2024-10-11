import urllib.request
import json
from django.shortcuts import render, redirect
from .models import Member
from . forms import MemberForm
# Create your views here.
def home(request):
    all_Members = Member.objects.all

    return render(request, 'home.html', {'all':all_Members})

def addMember(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect('/membersList')  # Redirect to a success page after submission
    else:
        form = MemberForm()
    
    return render(request, 'addMember.html', {'form': form})

    def members_list(request):
         members = Member.objects.all()  # Fetch all members from the database
    return render(request, 'main/membersList.html', {'members': members})
