from django.contrib import admin
from .models import Message,CustomerUser,Costume,Review,Bookmark

admin.site.register(Message)
admin.site.register(Costume)
admin.site.register(Review)
admin.site.register(Bookmark)
admin.site.register(CustomerUser)


