from django.urls import path
from . import views

urlpatterns = [
    path('celery/<int:par1>/<int:par2>/', views.celery_test, name='celery_test'),
]
