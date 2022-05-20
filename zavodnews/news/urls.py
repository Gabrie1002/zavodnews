from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<slug:slug>/', views.news_tag, name='news_tag'),
    path('new/<int:pk>/', views.news_detail, name='news_detail'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
