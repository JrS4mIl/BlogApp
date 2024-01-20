from django.contrib import admin
from .models import Category,Blogs,Comment
# Register your models here
#
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','category','author','status','is_featured','created_at','update_at')
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_featured',)


admin.site.register(Category)
admin.site.register(Blogs,BlogAdmin)
admin.site.register(Comment)