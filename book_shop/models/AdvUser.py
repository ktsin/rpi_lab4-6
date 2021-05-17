from django.contrib.auth.models import AbstractBaseUser, User, AbstractUser
import django.db.models as model


class AdvUser(AbstractUser):
    RL = [("ADMIN", "Admin"), ("BASE", "Base user")]
    rl = model.CharField(max_length=100, choices=RL)
