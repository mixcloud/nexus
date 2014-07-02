from django.apps import AppConfig

class NexusConfig(AppConfig):
    def ready(self):
        self.module.autodiscover()


