from django.shortcuts import render, get_object_or_404
from .models import Filmovi

from django.views.generic import ListView

from django.db.models import Count


# Create your views here.
def filmovi(request):


    queryset = Filmovi.objects.all().order_by('-date')

    # common_tags = Filmovi.tags.most_common().annotate(num_times=Count('taggit_taggeditem_items')).order_by(
    #     '-num_times')



    context = {
        'queryset': queryset,
        # 'common_tags': common_tags
    }
    return render(request, 'filmovi.html', context)


class TaggedObjectListView(ListView):
    template_name = 'tag-cloud.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return Filmovi.objects.filter(tags__name__in=[self.kwargs.get('tag_slug')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('tag_slug')
        return context


def film_view(request, slug):

    film_detalj = get_object_or_404(Filmovi, slug=slug)

    context = {
        'film_detalj': film_detalj
    }
    return render(request, 'film_detail.html', context)
