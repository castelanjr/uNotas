# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from scraper import Scraper

from json_utils import obj2json

@csrf_exempt
def main(request):
	username = request.POST['username']
	password = request.POST['password']
	scraper = Scraper(username, password)
	data = scraper.scrap()

	return HttpResponse(obj2json(data), mimetype='application/json')

