from django.urls import path
from sms_sender.views import HomePageView, SendSMSAPI, StartPageView

urlpatterns = [
    path('', StartPageView.as_view(),name='StartPage'),
    path('home/', HomePageView.as_view(), name='HomePage'),
    path('send_sms', SendSMSAPI.as_view(), name='SendSMSAPI')
]
