from rest_framework import generics
from rest_framework import authentication, permissions

# Create your views here.
from shipping.models import Account, Service, Packaging
from shipping.serializers import AccountSerializer, ServiceSerializer, PackagingSerializer


class AccountList(generics.ListCreateAPIView):
    """
    List all the categories
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user.id, updated_by=self.request.user.id)


class AccountDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List the Account details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ServiceList(generics.ListCreateAPIView):
    """
    List all the categories
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user.id, updated_by=self.request.user.id)


class ServiceDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List the Service details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class PackagingList(generics.ListCreateAPIView):
    """
    List all the categories
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Packaging.objects.all()
    serializer_class = PackagingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user.id, updated_by=self.request.user.id)


class PackagingDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List the Packaging details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Packaging.objects.all()
    serializer_class = PackagingSerializer

