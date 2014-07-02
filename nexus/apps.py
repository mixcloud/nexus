from django.apps import AppConfig

class NexusConfig(AppConfig):
    name = 'nexus'
    label = 'nexus'
    
    def ready(self):
        from django.contrib import admin
        
        self.module.autodiscover()
        # Remove the default admin panel
        self.module.site.unregister(admin.site.app_name)

