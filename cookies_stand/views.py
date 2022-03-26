from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cookies
from .permissions import IsOwnerOrReadOnly
from .serializers import CookiesSerializer


class CookiesList(ListCreateAPIView):
    queryset = Cookies.objects.all()
    serializer_class = CookiesSerializer


class CookiesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Cookies.objects.all()
    serializer_class = CookiesSerializer
