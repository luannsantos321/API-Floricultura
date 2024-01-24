from rest_framework import generics
from .serializers import FlorSerializers
from .models import Flor



class FloresAPIView(generics.ListCreateAPIView):
    queryset = Flor.objects.all()
    serializer_class = FlorSerializers
   

class FlorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flor.objects.all()
    serializer_class = FlorSerializers




