from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .crawler import run

def crawling(request):
	ip = request.META.get('REMOTE_ADDR')
	if ip == '127.0.0.1':
		run()
	return render(request, 'crawler/index.html', {})
