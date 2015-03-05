from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


class ObtainAuthTokenCustom(ObtainAuthToken):
    """
    doc string:

    """
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        try:
            token = Token.objects.get(user=user)
            token.delete()
        finally:
            token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})


obtain_auth_token = ObtainAuthTokenCustom.as_view()
