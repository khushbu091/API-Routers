from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = EmployeeSerializer
    queryset = User.objects.all()
