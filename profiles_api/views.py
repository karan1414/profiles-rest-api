
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class HelloApiView(APIView):
    """ Test API View """

    def get(self, request, format=None):
        """ Returns a list of api view features """
        an_apiview = [
            "Uses HTTP methods as functions (get,post,put,patch,delete)",
            "It is similar to traditional django views",
            "Gives you control over application logic",
            "Is mapped manually to urls"
        ]

        return Response({"msg": "Hello world in api!", "an_apiview": an_apiview})
