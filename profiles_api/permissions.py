from rest_framework import permissions


# Basepermission class that drf provides for making our own custom permissions
class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile """
    # add has_object_permission function to the class to define permission class, which gets called every time a reequest is made to the api we assign our permission to. It return True or False to determine if user has permissions to make changes that the user is trying to do.

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile """
        # check if http method used in http request is a safe method
        # safe methods: methods that dont make any changes to the objects
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # check if the obj user is trying to update matches their authenticated user profile that is added to the authentication of the request.
        # when we authenticate a request in DRF it will assign the authenticated user profile to the request which we can use to compare the object being updated and they have the same id. 
        return obj.id == request.user.id

class updateOwnStatus(permissions.BasePermission):
    """ Allow users to update their own status """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to update own status """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id