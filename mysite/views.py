from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('you\'ve reached the main site index')