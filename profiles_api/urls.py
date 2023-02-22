from django.urls import path

from profiles_api.views import HelloApiView

urlpatterns = [
    path('hello/', HelloApiView.as_view()),
]
