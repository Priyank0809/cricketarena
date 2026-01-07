from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)  # Like a short text field
    country = models.CharField(max_length=50)  # Another text field
    
    def __str__(self):
        return self.name  # Makes it pretty in admin