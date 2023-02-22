
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles_api import serializers

# we will use this to tell our apiview what data to expect when making post put and patch request to our api

# Create your views here.
class HelloApiView(APIView):
    """ Test API View """

    # set the serializer as follows
    serializer_class = serializers.HelloSerializer
    # this says whenever there is a request expect input to be name with charfield with max length as specified

    def get(self, request, format=None):
        """ Returns a list of api view features """
        an_apiview = [
            "Uses HTTP methods as functions (get,post,put,patch,delete)",
            "It is similar to traditional django views",
            "Gives you control over application logic",
            "Is mapped manually to urls"
        ]

        return Response({"msg": "Hello world in api!", "an_apiview": an_apiview})

    def post(self, request):
        """ Create a hello msg with our name """

        # 1. retrive serializers and pass in data that was sent in request
        serializer = self.serializer_class(data=request.data)
        # self.serializer_class() is a class func that comes with ApiView to retrieve the configured serializer class for our view.

        # 2. assign the data data=request.data to the serilizer class and assign to var for serializer class called serializer

        # 3. validate the input as per specification of serializer fields.
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name} !"

            return Response({"message": message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """ To update the entire object  """
        return Response({'method': "PUT"})

    def patch(self, request, pk=None):
        """ To update partial object """
        return Response({'method': "Patch"})

    def delete(self, request, pk=None):
        """ To delete an object """
        return Response({'method': "Delete"})