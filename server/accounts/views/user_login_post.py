from django.contrib.auth import login
from knox.views import LoginView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from server.accounts.serializers.login_serializer import LoginSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login_view(request) -> Response:
    """User login view"""

    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.validated_data['user']
        login(request, user)

        login_view = LoginView()
        login_view.request = request._request
        login_view.format_kwarg = None
        response = login_view.post(request=request)

        response_data = {
            'token': response.data.get('token'),
            'expire': response.data.get('expiry'),
        }

        return Response(response_data, status=status.HTTP_200_OK)

    else:
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
