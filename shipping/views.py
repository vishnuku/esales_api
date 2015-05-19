from rest_framework import generics
from rest_framework import authentication, permissions

# Create your views here.
from shipping.models import Account
from shipping.serializers import AccountSerializer


class AccountList(generics.ListCreateAPIView):
    """
    List all the categories
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_by=self.request.user, updated_by=self.request.user)


class AccountDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List the Account details
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

