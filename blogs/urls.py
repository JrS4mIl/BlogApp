from django.urls import path
from .views import post_by_category
urlpatterns = [
    path('<int:category_id>',post_by_category,name='category_post')

]