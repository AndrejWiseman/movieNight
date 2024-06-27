
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from filmovi.views import TaggedObjectListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('filmovi/', include('filmovi.urls')),

    path('tags/<slug:tag_slug>/', TaggedObjectListView.as_view(), name='tagged_objects_list'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

