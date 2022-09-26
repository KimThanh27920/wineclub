from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework_simplejwt import authentication

from . import serializers
from .. import models


class ListCreateCustomerAddressAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.AddressSerializer

    def get_queryset(self):
        queryset = models.Address.objects.filter(
            account_id=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(account = self.request.user)

class RetrieveUpdateDestroyCustomerAddressAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = serializers.AddressSerializer
    lookup_url_kwarg = "address_id"

    def get_queryset(self):
        queryset = models.Address.objects.filter(
            account_id=self.request.user.id)
        return queryset


#     def update(self, request, *args, **kwargs):
#         # update info delivery
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # update address
#         address = models.Address.objects.get(id = request.data['address']['id'])
#         serializer_address = serializers.AddressSerializer(address, data=request.data['address'], partial=True)
#         serializer_address.is_valid(raise_exception=True)
#         serializer_address.save()
#         return Response(serializer.data)


    