from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.serializers import UserLoginSerializer, UserRegisterSerializer, UserProfilesSerializer


class UserConfirmationView(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        confirmation_code = request.data.get('confirmation_code')
        if not confirmation_code:
            return Response({"error": "Не указан confirmation_code."}, status=status.HTTP_400_BAD_REQUEST)

        user = get_user_model().objects.filter(confirmation_code=confirmation_code).first()
        if not user:
            return Response({"error": "Неверный confirmation_code."}, status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.confirmation_code = None
        user.save()

        return Response({"message": "Пользователь успешно подтвержден."}, status=status.HTTP_200_OK)


class RegisterView(GenericAPIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user_model().objects.create_user(is_active=False, **serializer.validated_data)
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                'token': token.key,
                'data': serializer.data,
            }
        )


class LoginAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)

        if user:
            if not user.is_active:
                return Response({'error': 'User is not active!'})
            token, created = Token.objects.get_or_create(user=user) # (token, True) or (token, False)

            return Response(
                {
                    'token': token.key,
                    'username': user.username,
                    'email': user.email,
                }
            )

        return Response({'error': 'Wrong credentials!'})


class LogoutAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def logout(request):
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logout!'})


class ProfileView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfilesSerializer(instance=request.user, many=False)
        return Response(serializer.data)