from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from shop.models import EmailEntry
from datetime import datetime
import urllib
from xml.dom import minidom

def index(request):
	print request.META['HTTP_HOST']
	if request.META['HTTP_HOST'] == 'localhost:8000':
		return HttpResponseRedirect('/opkikker')
	else:
		return HttpResponseRedirect('/rustgever')

def opkikker(request):
		if request.POST:
			form = EmailEntry.Form(request.POST)
			if form.is_valid():
				email = form.cleaned_data['email']
				EmailEntry.objects.get_or_create(email=email, date_added=datetime.now())
				form.clean()
				return direct_to_template(request, 'opkikker.html', extra_context={'succes': True})
			else:
				return direct_to_template(request, 'opkikker.html', extra_context={'error': True, 'form': form,})
		else:
			form = EmailEntry.Form()
			return direct_to_template(request, 'opkikker.html', extra_context={'form': form})
			
def rustgever(request):
	return direct_to_template(request, 'rustgever.html')
	
def order(request):
	return direct_to_template(request, 'bestel-rustgever.html')
	
def pay(request, amount):
	URL = "https://secure.mollie.nl/xml/ideal?a=create-link&partnerid=705747&amount="+str(amount)+"&description=Zen%20Garden%20Rustgever(tm)&profile_key=e510805f"
	print URL
	result = urllib.urlopen(URL).read()
	splits = result.split("<URL>")
	return HttpResponse(splits[1].split("</URL>")[0])
		

