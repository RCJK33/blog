from django.urls import path
from .views import AboutTemplateView, HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(),name='home'),
    path('about/', AboutTemplateView.as_view(),name='about'),
]