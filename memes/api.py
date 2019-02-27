from rest_framework.viewsets import ModelViewSet
from .models import Memes
from .serializers import MemeSerializer


class MemeViewSet(ModelViewSet):
    queryset = Memes.objects.all()
    serializer_class = MemeSerializer