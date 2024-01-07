from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer


class RegistrationView(APIView):
    @staticmethod
    def post(request):
        if request.user.is_authenticated:
            return Response({'ok': False, 'message': 'You are already registered'})
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except Exception as e:
            print(type(e), e, sep='\n')
            return Response({'ok': False, 'message': f'{e}'})
        authenticate(request, username=request.data['username'], password=request.data['password'])
        login(request, request.user)
        return Response({'ok': True, 'message': 'successfully logged in'})

    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return Response({'ok': True, 'message': 'user exists', 'user': UserSerializer(request.user).data})
        return Response({'ok': False, 'message': 'user does not exist'})

    @staticmethod
    def delete(request):
        if request.user.is_authenticated:
            logout(request)
            request.user.delete()
            return Response({'ok': True, 'message': 'account successfully deleted'})
        return Response({'ok': False, 'message': 'user does not exist'})


class LoginView(APIView):

    @staticmethod
    def post(request):
        if not request.user.is_authenticated:
            return Response({'ok': False, 'message': 'user does not registered in this account'})
        if not request.user.username == request.data['username']:
            return Response({'ok': False, 'message': 'invalid username'})
        if not request.user.check_password(request.data['password']):
            return Response({'ok': False, 'message': 'wrong password'})
        login(request, request.user)
        return Response({'ok': True, 'message': 'successfully logged in'})

    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return Response({'ok': True, 'message': 'user logged in', 'user': UserSerializer(request.user)})
        return Response({'ok': False, 'message': 'user does not logged in or does not exist'})

    @staticmethod
    @login_required(login_url='login')
    def delete(request):
        if request.user.is_authenticated:
            logout(request)
            return Response({'ok': True, 'message': 'user logged out'})
        return Response({'ok': False, 'message': 'user does not logged in or does not exist'})
