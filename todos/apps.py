from django.apps import AppConfig

class TodosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Add this line
    name = 'todos'