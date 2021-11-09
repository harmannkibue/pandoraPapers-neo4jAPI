from django.apps import AppConfig


class FetchApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fetch_api'

    def ready(self):
        from papers_search import constants
