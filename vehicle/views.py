from django.shortcuts import render
from django.views import generic, View 
from .models import *

class Home(generic.TemplateView):
    '''
    Home page view
    '''
    template_name='index.html'

def search(request):
    '''
    search results
    '''
    # Get all vehicle data
    queryset = Vehicle.objects.all()

    if request.POST:
        searched = request.POST["searched"]
        results = Vehicle.objects.filter(Q(title__contains=searched) |
                                     Q(brand__contains=searched) |
                                     Q(content__contains=searched)
                                    ).distinct()
        context = {'queryset': queryset}

        return render(request, 'vehicle/search.html', {'results': results, 'searched': searched})
    else:
        return render(request, 'vehicle/search.html', context)


