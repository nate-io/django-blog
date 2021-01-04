from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # utilize the User -> Profile model mapping
    def ready(self):
        import users.signals
