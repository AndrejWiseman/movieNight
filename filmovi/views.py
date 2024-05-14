from django.shortcuts import render
from .models import Filmovi


# Create your views here.
def filmovi(request):

    queryset = Filmovi.objects.all().order_by('-date')

    context = {
        'queryset': queryset
    }
    return render(request, 'filmovi.html', context)
