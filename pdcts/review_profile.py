from Nuaza.pdcts.models import ProductReview
from Nuaza.pdcts.forms import ProductReviewForm

def retrieve(request, review_slug):
    try:
        profile = ProductReview.objects.get(user=request.user, slug=review_slug)
    except ProductReview.DoesNotExist:
        profile = ProductReview(user=request.user)
#        profile.save()
    return profile
    
def set(request, review_slug):
    """ updates the information stored in the user's profile """
    profile = retrieve(request, review_slug)
    profile_form = ProductReviewForm(request.POST, request.FILES, instance=profile)
    profile_form.save()
    
