from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('fais', views.home, name='fais-home'),
    path('fais/data', views.data, name='data'),
    path('fais/upload', views.upload, name='upload'),
    path('fais/userdata', views.userdata, name='userdata'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)