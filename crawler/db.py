from .models import Movie


def save(title, date, point, site):
	movies = Movie.objects.filter(title=title)
	if len(movies) == 0:
		Movie.objects.create(title=title, realesedate=date)

	movie = Movie.objects.get(title=title)

	if 'RT' == site:
		movie.rt = point
	elif 'DAUM' == site:
		movie.daum = point
	elif 'METAC' == site:
		movie.metac = point

	movie.save()
