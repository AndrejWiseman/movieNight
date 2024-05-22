from django.shortcuts import render, get_object_or_404
from .models import Filmovi


# Create your views here.
def filmovi(request):

    queryset = Filmovi.objects.all().order_by('-date')

    context = {
        'queryset': queryset
    }
    return render(request, 'filmovi.html', context)




def film_view(request, slug):

    film_detalj = get_object_or_404(Filmovi, slug=slug)

    context = {
        'film_detalj': film_detalj
    }
    return render(request, 'film_detail.html', context)
