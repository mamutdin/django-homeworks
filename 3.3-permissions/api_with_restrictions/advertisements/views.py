from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, AdvertisementStatusChoices
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = AdvertisementFilter

    def get_queryset(self):
        filter_params = Q(status=AdvertisementStatusChoices.OPEN)
        if self.request.user.is_authentificated:
            filter_params |= Q(creator=self.request.user)
        return Advertisement.objects.filter(filter_params)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.request.method in SAFE_METHODS:
            return []
        return [IsAuthenticated(), IsOwner()]