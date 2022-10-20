from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('helloworld.html')
  return HttpResponse(template.render())
  # return HttpResponse("Hello world!")