from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from api.auth.serializers import CustomUserSignUpSerializer


@api_view(['POST'])
def user_signup(request):
    """
    Регистрация пользователя с передачей параметров через тело запроса.
    """
    serializer = CustomUserSignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    # Генерируем токены
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    return Response({
        'access': access_token,
        'refresh': refresh_token
    }, status=status.HTTP_201_CREATED)