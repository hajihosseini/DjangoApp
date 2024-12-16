from django.contrib import admin

from .models import Question, Choice

# # Unregister the model if it's already registered  
# admin.site.unregister(Question)  
# admin.site.unregister(Choice)  

# Now register them again  
admin.site.register(Question)  
admin.site.register(Choice)