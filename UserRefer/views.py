from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Invitation
from .serializers import InvitationSerializer, UserListSerializer
import uuid


class InvitationView(generics.ListCreateAPIView):
    serializer_class = InvitationSerializer

    def get_queryset(self):
        queryset = Invitation.objects.all()
        # queryset = Invitation.objects.filter(username=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            invite_code=uuid.uuid1())


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class InvitationMatchView(generics.ListAPIView):
    serializer_class = InvitationSerializer

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q')
        queryset = Invitation.objects.filter(invite_code=query)
        return queryset
