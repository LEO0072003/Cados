from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('', views.endpoints),

    path('advocate/', views.advocate_list , name='advocates'),  # type: ignore

    path('advocate/<str:username>/', views.AdvocateDetail.as_view()),
    path('companies/', views.companyList),

]
