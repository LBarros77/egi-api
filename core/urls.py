from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.Overview.as_view()),
    path('eventos/', views.EventList.as_view()),
    path('eventos/<int:pk>', views.EventDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns.append(path('api-auth/', include('rest_framework.urls')))

urlpatterns = format_suffix_patterns(urlpatterns)