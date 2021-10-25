from django.urls import path
from . import views

app_name = 'MadLibsApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('madlibuserinput/', views.madlibuserinput, name='madlibuserinput'),
    path('madlibsdisplay/', views.madlibsdisplay, name='madlibsdisplay'),

]
