from django.urls import path

from . import views

urlpatterns = [
    path('fixture/<int:fixture_id>/', views.index, name='fixture-details'),
    path('fixture/', views.fixture_home, name="fixture"),
]
