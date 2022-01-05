from django.urls import path
from userinfo import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('userinfo/', view=views.UserInfoList.as_view()),
    path('userinfo/<int:pk>/', views.UserInfoDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)