from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('rest/v1/calendar/init/',views.GoogleCalendarInitView,name='index'),
    path('rest/v1/calendar/redirect/',views.GoogleCalendarRedirectView,name='events'),

]