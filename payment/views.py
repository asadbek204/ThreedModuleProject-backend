from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from payment.serializers import *


class CRUDView:
    permission_classes = [IsAuthenticated]

    def __init__(self, model, serializer, name: str):
        self.model = model
        self.serializer = serializer
        self.name = name

    def get(self, request) -> Response:
        data = self.model.objects.filter(user=request.user)
        ok = data.exists()
        data = self.serializer(data, many=True).data
        return Response(
            {
                'ok': ok,
                'message': f'successfully found {self.name}' if ok else f'no {self.name} found',
                self.name: data
            }
        )

    def post(self, request) -> Response:
        data = request.data
        data.update(user=request.user.id)
        print(data)
        serializer = self.serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True, 'message': 'successful'})
        return Response({'ok': False, 'message': 'wrong data', 'errors': serializer.errors})

    def delete(self, request) -> Response:
        try:
            data = self.model.objects.get(id=request.data[f'{self.name}_id'], user=request.user)
        except self.model.DoesNotExist:
            return Response({'ok': False, 'message': f'{self.name} not found'})
        else:
            data.delete()
            return Response({'ok': True, 'message': f'{self.name} successfully deleted'})

    def patch(self, request) -> Response:
        data = self.model.objects.get(id=request.data[f'{self.name}_id'], user=request.user)
        serializer = self.serializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True, 'message': f'{self.name} successfully updated'})
        return Response({'ok': False, 'message': 'wrong data', 'errors': serializer.errors})

    def __call__(self, cls):
        cls.model = self.model
        cls.serializer = self.serializer
        cls.name = self.name
        cls.get = self.get
        cls.post = self.post
        cls.patch = self.patch
        cls.delete = self.delete
        return cls


@CRUDView(model=Payment, serializer=PaymentSerializer, name='payment')
class PaymentView(APIView):
    permission_classes = [IsAuthenticated]


@CRUDView(model=Order, serializer=OrderSerializer, name='order')
class OrderView(APIView):
    permission_classes = [IsAuthenticated]


@CRUDView(model=Card, serializer=CardSerializer, name='card')
class CardView(APIView):
    permission_classes = [IsAuthenticated]


@CRUDView(model=Wallet, serializer=WalletSerializer, name='wallet')
class WalletView(APIView):
    permission_classes = [IsAuthenticated]

