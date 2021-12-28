from django.db import models

class Configuration(models.Model):
    config = models.CharField(max_length=30)
    value = models.CharField(max_length=20)

    class Meta:
        db_table = 'configuration'
    
    def __str__(self) -> str:
        return self.config
