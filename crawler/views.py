from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .crawler import run

def crawling(request):
	run()
	return render(request, 'index.html', {})
