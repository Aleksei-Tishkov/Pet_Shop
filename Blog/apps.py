from django.apps import AppConfig
from django.core.signals import request_finished


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blog'

    from . import signals
    request_finished.connect(signals.post_save_post)
