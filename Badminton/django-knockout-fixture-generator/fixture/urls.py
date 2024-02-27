from django.urls import path

from . import views

urlpatterns = [
    path('<int:fixture_id>/', views.indexf, name='fixture'),
]
