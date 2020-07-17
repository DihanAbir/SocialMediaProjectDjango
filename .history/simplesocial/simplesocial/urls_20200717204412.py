from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('accounts.urls', namespace=accounts)),
    path('', views.HomePage.as_view(), name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
