################################################################################
from django.urls import path
from . import views
from .views import (
    BoxListView,
    BoxDetailView,
    ActivityListView,
    ActivityDetailView
)

################################################################################
app_name = 'box'
################################################################################
urlpatterns = [
    path('', BoxListView.as_view(), name='box_list'),
    path(
        '<int:id>/',
        BoxDetailView.as_view(),
        name='box_detail'
    ),
    path(
        '<int:id>/activity/',
        ActivityListView.as_view(),
        name='activity_list'
    ),
    path(
        '<int:id>/activity/<int:pk>/',
        ActivityDetailView.as_view(),
        name='activity_detail'
    ),
]
################################################################################
