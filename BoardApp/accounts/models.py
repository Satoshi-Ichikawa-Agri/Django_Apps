from uuid import uuid4
from datetime import datetime, timedelta
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.dispatch import receiver


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    picture = models.FileField(null=True, upload_to='picture/')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class UserActivateTokensManager(models.Manager):
    
    def activate_user_by_token(self, token):
        user_activate_token = self.filter(
            token=token,
            expired_at__gte=datetime.now()
            ).first()
        user = user_activate_token.user
        user.is_active = True
        user.save()


class UserActivateTokens(models.Model):
    token = models.UUIDField(db_index=True)
    expired_at = models.DateTimeField()
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

    objects = UserActivateTokensManager()

    class Meta:
        db_table = 'user_activate_tokens'


@receiver(post_save, sender=Users)
def publish_token(sender, instance, **kwargs):
    user_activate_token = UserActivateTokens.objects.create(
        user=instance,
        token=str(uuid4()),
        expired_at=datetime.now() + timedelta(days=1)
        )
    # メールでURLを送る方がよいが、今回はprintでターミナル上に表示する
    print(f'http://127.0.0.1:8000/accounts/activate_user/{user_activate_token.token}')
