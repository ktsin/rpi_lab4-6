from django.contrib.auth.models import AbstractBaseUser
import django.db.models as model


class AdvUser(AbstractBaseUser):
    Rl = [("ADMIN", "Admin"), ("BASE", "Base user")]
    rl = model.CharField(max_length=100, choices=Rl)