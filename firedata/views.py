from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .forms import *

from .models import *

# Create your views here.
        
def index(request):
    events = BurningEvent.objects.select_related('conservation_unit')
    return render(request, 'firedata/index.html', {'events': events})