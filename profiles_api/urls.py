from django.urls import include, path
from rest_framework.routers import DefaultRouter

from profiles_api.views import (HelloApiView, HelloViewSet, UserLoginApiView,
                                UserProfileViewSet)

router = DefaultRouter()
# this will create the full url for us so we do not need to specify /
router.register('hello_viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewSet)
# no need to assign basename as queryset is provided in viewset and DRF can figure out the name from the name assigned to it. 
# provide base name only if there is no queryset or we want to override the queryset associated to the view.

urlpatterns = [
    path('hello/', HelloApiView.as_view()),
    path('login/', UserLoginApiView.as_view()),
    # as we register new routes with router it generates list of all urls for our viewset
    path('', include(router.urls))
]

# to register ViewSets we use router that is a class provided by drf in order to generate diff router available for our viewSet.
#  
