from django.apps import AppConfig


class VehicleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicle'

    def ready(self):
        """
        Boardcast user's signal to app
        """
        import vehicle.signals
