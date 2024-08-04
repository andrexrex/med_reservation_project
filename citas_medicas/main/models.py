from django.db import models

class Contact(models.Model):
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15, blank=True)
    message = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.customer_name} {self.customer_email}"