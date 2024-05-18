from django.apps import AppConfig
import atexit
class EssentialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'essential'
    def ready(self):
        # Delay imports until the app registry is ready
        from essential.utils.threading import PeriodicTask
        from essential.views import delete_expired_tasks
        
        interval = 24 * 60 * 60  # 24 hours
        self.task = PeriodicTask(interval, delete_expired_tasks)
        self.task.start()
    
        atexit.register(self.shutdown)

    def shutdown(self):
        self.task.stop()
