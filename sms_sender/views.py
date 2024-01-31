from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from mkvgroup_test_project.settings import TWILLIO_AUTH_TOKEN, TWILLIO_ACCOUNT_SID, TWILLIO_NUMBER
from twilio.rest import Client

import logging

sms_logger = logging.getLogger('sms_requests')


class StartPageView(View):
    def get(self, request):
        return render(request, 'index.html')


class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')


class SMSSendingExceprion(Exception):
    pass


class SendSMSAPI(APIView):

    def post(self, request):
        phone_number = request.data['phone_number']
        message = request.data['message']
        try:
            self.send_sms(phone_number, message)
        except SMSSendingExceprion:
            return render(request, 'error.html')

        return render(request, 'success.html', )

    def send_sms(self, phone_number: str, message: str):
        client = Client(TWILLIO_ACCOUNT_SID, TWILLIO_AUTH_TOKEN)
        message = client.messages.create(
            from_=TWILLIO_NUMBER,
            body=message,
            to=phone_number,
        )
        if message.error_message:
            sms_logger.info(f'Something went wrong, error message: {message.error_message}')
            raise SMSSendingExceprion()
        else:
            sms_logger.info(f'SMS was successfully sent to {phone_number}')







