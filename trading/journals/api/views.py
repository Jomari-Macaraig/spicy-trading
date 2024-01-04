from rest_framework import generics

from .serializers import JournalSerializer
from ..models import Journal


class JournalList(generics.ListAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
