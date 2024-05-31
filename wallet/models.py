import uuid
from django.db import models
from user.models import User
# Create your models here.


class WalletModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    balance = models.DecimalField(default=0.00,decimal_places=2,max_digits=11)
    user = models.OneToOneField( User, on_delete=models.CASCADE,editable=False)
    
    def __str__(self) -> str:
        return self.user