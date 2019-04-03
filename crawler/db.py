from .models import Movie
from django.core.exceptions import ObjectDoesNotExist

def save(title, date, point, site):
	"""
	movies = Movie.objects.filter(title=title)
	if len(movies) == 0:
		movie = Movie.objects.create(title=title, realesedate=date)
	else :
		movie = movies[:1]
	"""
	try :
		movie = Movie.objects.get(title=title)
	except Movie.DoesNotExist:
		movie = Movie.objects.create(title=title, releasedate=date)	
	except ObjectDoesNotExist:
		movie = Movie.objects.create(title=title, releasedate=date)	
	except Exception as ex:
		print("Exception : " , ex)		

	if 'RT' == site:
		movie.rt = point
	elif 'DAUM' == site:
		movie.daum = point
	elif 'METAC' == site:
		movie.metac = point

	movie.save()
