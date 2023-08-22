from django.urls import path
from . import views
from .views import submit_patient

app_name = 'billingapp'

urlpatterns = [
    path('submit/', views.submit_patient, name='submit_patient'),
    path('success/', views.success, name='success'),
]
