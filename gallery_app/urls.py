from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^$',views.galleries,name='galleries'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_gallery,name='pastGallery'),
    url(r'^search/tag/',views.tag_results,name='tag_results'),
    url(r'^search/category/',views.category_results,name='category_results'),
    url(r'^search/location/',views.location_results,name='location_results'),
    url(r'^image/(\d+)/$',views.image,name='image')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)