from django.contrib.auth.backends import ModelBackend
from .models import CustomerUser

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try to authenticate with CustomerUser
        try:
            user = CustomerUser.objects.get(email=username)
        except CustomerUser.DoesNotExist:
            try:
                user = CustomerUser.objects.get(username=username)
            except CustomerUser.DoesNotExist:
                    return None

        if user.check_password(password):
            return user
        return None