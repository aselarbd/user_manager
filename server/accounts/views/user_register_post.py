from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from server.accounts.serializers.create_user_serializer import CreateUserSerializer

WHITELIST_FIELDS = ('email', 'first_name', 'last_name', 'date_of_birth', 'is_active')


def _filter_output_data(data: dict) -> dict:
    return {field: data.get(field) for field in WHITELIST_FIELDS if field in data}


@api_view(['POST'])
@permission_classes([AllowAny])
def user_create_view(request) -> Response:
    """Create user view"""

    serializer = CreateUserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        created_user = _filter_output_data(data=serializer.data)
        return Response(data=created_user, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
