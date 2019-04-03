from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from crawler.models import Movie

def main(request):
	movie = Movie.objects.filter(releasedate__lte=timezone.now()).order_by('-releasedate')
	movie = movie[:20]
	return render(request, 'mysite/index.html', {'movies': movie})
			
