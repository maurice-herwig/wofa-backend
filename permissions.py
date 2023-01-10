from rest_framework import permissions
from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication


class ClientAuthorization(permissions.BasePermission):

    def has_permission(self, request, view):
        """ Override the has_permission method from BasePermission.
            This class allowed the access only clients that have a correct access_token.
        """
        return bool(request.successful_authenticator and
                    isinstance(request.successful_authenticator, OAuth2Authentication))
