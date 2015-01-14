from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	metrowest = {'start_latitude':'34.019454','start_longitude':'-118.491191','end_latitude':'42.353743','end_longitude':'-71.066451'}
	NewtonBC = {'start_latitude':'33.881728','start_longitude':'-118.404121','end_latitude':'42.353743','end_longitude':'-71.066451'}
	Cambridge = {'start_latitude':'34.085036','start_longitude':'-118.359318','end_latitude':'42.353743','end_longitude':'--71.066451'}
	financial = {'start_latitude':'34.069112','start_longitude':'-118.281384','end_latitude':'42.353743','end_longitude':'-71.066451'}
	Southie = {'start_latitude':'34.057166','start_longitude':'-118.323956','end_latitude':'42.353743','end_longitude':'-71.066451'}
	
	cities = []
	cities.append(metrowest)
	cities.append(NewtonBC)
	cities.append(Cambridge)
	cities.append(financial)
	cities.append(southie)
)
	info = ''
	names = ["Metrowest","NewtonBC","Cambridge","financial","southie"]

	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token ZzTuXujgb8xTD64LILYh0sxA3uDmsw_6xKtaok9w'}
		r = requests.get('https://api.uber.com/v1/estimates/price', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + (names[cities.index(i)]) + '    '
		info = info + (data['prices'][0]['display_name']) + '    '
		info = info + str((data['prices'][0]['surge_multiplier'])) + '  <br/><br/>'	
	return HttpResponse(info)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

