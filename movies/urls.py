from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('contact/', views.contact, name='contact'),
    path('thankyou/',  TemplateView.as_view(template_name="movies/thankyou.html"), name='thankyou')
]
