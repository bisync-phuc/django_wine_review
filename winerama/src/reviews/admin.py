from django.contrib import admin

# Register your models here.
from .models import Review, Wine


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('wine', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']


assert isinstance(admin.site.register, object)
admin.site.register(Wine)
admin.site.register(Review, ReviewAdmin)
