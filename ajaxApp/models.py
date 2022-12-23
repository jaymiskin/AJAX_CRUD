from django.db import models

# Create your models here.
class User(models.Model):
    FullName = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)
    Technology = models.CharField(max_length=30)

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.FullName