from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.db import models
from django.contrib.sessions.base_session import AbstractBaseSession
from users.models import User

class CustomSession(AbstractBaseSession):
    name = 'session_app'
    account_id = models.IntegerField(null=True, db_index=True)
    name = models.TextField(null=True)
    role = models.TextField(null=True)

    @classmethod
    def get_session_store_class(cls):
        return DBStore

class SessionStore(DBStore):
    @classmethod
    def get_model_class(cls):
        return CustomSession

    def create_model_instance(self, data):
        obj = super().create_model_instance(data)
        try:
            account_id = int(data.get('_auth_user_id'))
        except (ValueError, TypeError):
            account_id = None
        obj.account_id = account_id
        if account_id is not None:
            user = User.objects.get(pk=account_id)
            obj.name = user.get_full_name()
            obj.role = user.role
        return obj