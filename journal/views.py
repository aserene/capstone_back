from django.shortcuts import render
from .models import Entry
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EntrySerializer
# Create your views here.
class EntryViewSet (viewsets.ModelViewSet):
    queryset=Entry.objects.all()
    serializer_class=EntrySerializer
    permission_classes=[permissions.AllowAny]