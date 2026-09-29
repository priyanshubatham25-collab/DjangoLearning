import datetime 
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f'[{datetime.datetime.now()}] request url:{request.path}')

    def process_response(self, request, response):
        print(f"[{datetime.datetime.now()}] response status:{response.status_code}")
        return response 