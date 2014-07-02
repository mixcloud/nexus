from django.apps import AppConfig

class NexusConfig(AppConfig):
    name = 'nexus'
    label = 'nexus'
    
    def ready(self):
        self.module.autodiscover()


