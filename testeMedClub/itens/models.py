import uuid
from django.db import models
# Create your models here.

class item(models.Model):
    id_item = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    #description = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

