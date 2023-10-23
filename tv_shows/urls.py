from django.urls import path
from . import views

urlpatterns = [
    path('',views.tvShowListView),
    path('show_detail/<int:id>/',views.tvShowDetailView),
]