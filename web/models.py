from django.db import models
import uuid

# Create your models here.

class Flan(models.Model):
    flan_uuid=models.UUIDField()
    name= models.CharField(max_length=64)
    description=models.TextField(default='')
    image_url=models.URLField(default='')
    slug=models.SlugField(default='')
    is_private=models.BooleanField(default=True)
    precio=models.IntegerField()
    #con esto muestra los nombres en la lista de, en este caso, flanes.
    # def __str__(self):
    #     return self.name
    #con esto muestra los nombres e id en la lista de, en este caso, flanes.
    def __str__(self):
        return f"{self.name} ({self.id})"
    


#crear modelo de contactform

class ContactForm(models.Model):
    contact_form_uuid= models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email=models.EmailField()
    customer_name=models.CharField(max_length=64)
    message=models.TextField()

class Contact(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name