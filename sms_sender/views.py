from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from twilio.base.exceptions import TwilioRestException, TwilioException

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


class ErrorPageView(View):
    def get(self, request):
        return render(request, 'error.html')


class SuccessPageView(View):
    def get(self, request):
        return render(request, 'success.html')


class SMSSendingException(Exception):
    pass


class SendSMSAPI(APIView):

    def post(self, request):
        phone_number = request.data['phone_number']
        message = request.data['message']
        try:
            self.send_sms(phone_number, message)
            return render(request, 'success.html', )
        except SMSSendingException:
            return render(request, 'error.html')

    def send_sms(self, phone_number: str, message: str):
        try:
            client = Client(TWILLIO_ACCOUNT_SID, TWILLIO_AUTH_TOKEN)
        except TwilioException as error:
            sms_logger.info(f'Something went wrong, error message: {error}')
            raise SMSSendingException()
        try:
            new_message = client.messages.create(
                from_=TWILLIO_NUMBER,
                body=message,
                to=phone_number,
            )
        except TwilioRestException as error:
            sms_logger.info(f'Something went wrong, error message: {error.msg}')
            raise SMSSendingException()
        else:
            sms_logger.info(f'SMS was successfully sent to {phone_number}')







