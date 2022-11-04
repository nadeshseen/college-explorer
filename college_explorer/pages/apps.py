from django.apps import AppConfig


class PagesConfig(AppConfig):
    """
    Inbuilt class of django

    This file is created to help the user include any application configuration for the app. Using this, you can configure some of the attributes of the application.
    Reference(https://stackoverflow.com/questions/32795227/what-is-the-purpose-of-apps-py-in-django-1-9)
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
