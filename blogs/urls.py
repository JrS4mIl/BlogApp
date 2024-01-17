from django.urls import path
from .views import post_by_category,single_blog
urlpatterns = [
    path('<int:category_id>',post_by_category,name='category_post'),


]