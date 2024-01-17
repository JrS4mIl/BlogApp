from .models import Category
from assignments.models import SocialMedia
def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)
def get_social(request):
    socialLink=SocialMedia.objects.all()
    return dict(socialLink=socialLink)