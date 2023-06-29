from django.urls import path
from . import views

urlpatterns=[
    path('setdata/', views.index, name='setdata'),
    path('setdata/<int:question_id>/', views.detail),
]