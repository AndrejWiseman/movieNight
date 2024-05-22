from django.shortcuts import render, get_object_or_404

from filmovi.models import Filmovi


# Create your views here.
def index(request):

    filmovi = Filmovi.objects.all().order_by('-date')

    context = {
        'filmovi': filmovi,
    }
    return render(request, 'index.html', context)
