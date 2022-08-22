from django.contrib import admin
from django.urls import path, include
from .views import AssignmentListCreate, AssignmentRetrieveUpdateDestroy, CourseChapterListCreate, CourseChapterRetrieveUpdateDestroy, CourseListCreate, CourseRetrieveUpdateDestroy
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import  RegisterAPI

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [


    path('assignment/', AssignmentListCreate.as_view()),
    path('assignment/<uuid:pk>/', AssignmentRetrieveUpdateDestroy.as_view()),


    path('coursechap/', CourseChapterListCreate.as_view()),
    path('coursechap/<uuid:pk>/', CourseChapterRetrieveUpdateDestroy.as_view()),


    path('course/', CourseListCreate.as_view()),
    path('course/<uuid:pk>/', CourseRetrieveUpdateDestroy.as_view()),

    path('api/register/', RegisterAPI.as_view(), name='register'),



    # path('auth/login/', TokenObtainPairView.as_view(), name='create-token'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rest-auth/', include('rest_auth.urls')),
]