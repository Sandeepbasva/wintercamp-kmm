from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.


def persons(request):
    response = HttpResponse()
    response.write('<html><body>')
    response.write('<h1>Details</h1>')
    person_list = Person.objects.all()
    for person in person_list:
        response.write('<li>%s%s</li>'%(person.id, person.name))
    response.write('</body></html>')
    return response


def details(request, pid):
    pid = int(pid)
    response = HttpResponse()
    response.write('<html><body>')
    try:
        person = Person.objects.get(id=pid)
        response.write('<h1>Details of Person %s</h1><hr>'%person.name)
        response.write('<li>Gender: %s</li>'%person.gender)
        response.write('<li>Birthday: %s</li>'%person.birthday)
        response.write('<li>Favourite URL: %s</li>'%person.url)
        response.write('<li>Message: %s</li>'%person.bio)
    except:
        print('The person details does not exist')
    response.write('</body></html>')
    return response
