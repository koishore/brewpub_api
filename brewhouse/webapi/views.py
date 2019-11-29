from django.http import HttpResponse
from django.db.models import Q
from django.template import loader
from .models import Brewery
import json

def index(request):
    return HttpResponse("Koishore's API for Brewpubs")

def search(request):
    template=loader.get_template('webapi/search.html')
    return_list = []
    query=request.GET.get('q')
    if query:
        brew = Brewery.objects.all().filter(Q(name__icontains=query) |
                                            Q(type__icontains=query) |
                                            Q(state__icontains=query) |
                                            Q(website__icontains=query) |
                                            Q(address__icontains=query)).distinct()
    else:
        brew = []
    data = {}
    for each in brew:
        try:
            data[each.name].append({'type' : each.type,
                                    'state' : each.state,
                                    'address' : each.address,
                                    'website' : each.website})
        except KeyError:
            data[each.name] = [{'type' : each.type,
                                'state' : each.state,
                                'address' : each.address,
                                'website' : each.website}]
    context = {
        'data' : json.dumps(data),
    }
    return HttpResponse(template.render(context, request))
