from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import UserSerializer
from django.utils.translation import gettext_lazy as _


class RegistrationView(APIView):
    @staticmethod
    def post(request):
        if request.user.is_authenticated:
            return Response({'ok': False, 'message': _('You are already registered')})
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            authenticate(request, username=request.data['username'], password=request.data['password'])
            login(request, user)
            return Response({'ok': True, 'message': _('successfully logged in')})
        return Response({'ok': False, 'message': _('wrong data'), 'errors': serializer.errors})

    @staticmethod
    def delete(request):
        if request.user.is_authenticated:
            request.user.check_password(request.data['password'])
            request.user.delete()
            return Response({'ok': True, 'message': _('account has been deleted')})
        return Response({'ok': False, 'message': _('user not registered')})


class LoginView(APIView):

    @staticmethod
    def post(request):
        try:
            user = User.objects.get(username=request.data['username'])
        except User.DoesNotExist:
            return Response({'ok': False, 'message': _('user does not exist')})
        else:
            if user.check_password(request.data['password']):
                login(request, user)
                return Response({'ok': True, 'message': _('successfully logged in')})
            return Response({'ok': False, 'message': _('wrong password')})

    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return Response({'ok': True, 'message': _('user is authenticated'), 'user': UserSerializer(request.user).data})
        return Response({'ok': False, 'message': _('user does not logged in or does not exist')})

    @staticmethod
    def patch(request):
        if not request.user.is_authenticated:
            return Response({'ok': False, 'message': _('user does not logged in or does not exist')})
        if not request.data.get('password'):
            return Response({'ok': False, 'message': _('please provide password')})
        if not request.user.check_password(request.data.pop('password')):
            return Response({'ok': False, 'message': _('wrong password')})
        if request.data.get('newpassword'):
            request.user.set_password(request.data['newpassword'])
            login(request, request.user)
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True, 'message': _('successfully updated user')})
        return Response({'ok': False, 'message': _('wrong parameters'), 'errors': serializer.errors})

    @staticmethod
    def delete(request):
        if request.user.is_authenticated:
            logout(request)
            return Response({'ok': True, 'message': _('user logged out')})
        return Response({'ok': False, 'message': _('user does not logged in or does not exist')})
