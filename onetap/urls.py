from django.urls import path

from .views import MainView

urlpatterns = [
    path('onetap/', MainView.as_view(), name='onetap'),
]
