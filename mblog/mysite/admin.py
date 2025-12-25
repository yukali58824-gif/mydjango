from django.contrib import admin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')


from mysite.models import Post
admin.site.register(Post,PostAdmin)
