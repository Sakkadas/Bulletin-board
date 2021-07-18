from django.urls import path

from .views import bbs, BbDetailView

urlpatterns = [
    path('bbs/<int:pk>/', BbDetailView.as_view()),
    path('bbs/', bbs),
]
