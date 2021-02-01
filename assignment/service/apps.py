from django.apps import AppConfig

# from django.core.signals import request_started

# from service.signal import log_request

class ServiceConfig(AppConfig):
    name = 'service'
    # def ready(self):
        # request_started.connect(log_request)
        # import service.signal
