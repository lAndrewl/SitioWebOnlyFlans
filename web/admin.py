from django.contrib import admin
from .models import Flan,Contact,ContactForm

# Register your models here.

admin.site.register(Flan)
admin.site.register(ContactForm)
admin.site.register(Contact)