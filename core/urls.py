from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.Overview.as_view()),
    path('eventos/', views.EventList.as_view()),
    path('evento/detailhe/<int:pk>', views.EventDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)