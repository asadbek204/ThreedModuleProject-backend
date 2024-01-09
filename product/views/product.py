from rest_framework.response import Response
from rest_framework.views import APIView
from product.serializers import *


class SubCatalogView(APIView):
    @staticmethod
    def get(request, gender=None, pk=None):
        return Response({'ok': True, 'message': 'success', 'products': ProductSerializer(Product.objects.filter(category_id=pk), many=True).data})


class ProductView(APIView):
    @staticmethod
    def get_material(material):
        result = {}
        result.update(name=material.name)
        result.update(fit=material.fit)
        result.update(compounds=CompoundSerializer(material.compounds, many=True).data)
        return result

    def product_detail(self, product):
        result = {}
        result.update(product=ProductSerializer(product).data)
        result.update(images=ImagesSerializer(product.images, many=True).data)
        result.update(material=self.get_material(product.material))
        result.update(parameters=ParameterSerializer(product.parameters, many=True).data)
        return result

    def get(self, request, gender=None, pk=None, p_id=None):
        try:
            product = Product.objects.get(id=p_id)
        except Product.DoesNotExist:
            return Response({'ok': False, 'message': 'wrong product id', 'errors': 'product not found'})
        return Response(
            {
                'ok': True,
                'message': 'success',
                'product': self.product_detail(product)
            }
        )


class ReviewView(APIView):
    @staticmethod
    def get(request, gender=None, pk=None, p_id=None, r_id=None):
        result = {
            'ok': True,
            'message': 'success',
        }
        if r_id:
            try:
                result.update(reviews=ProductReviewSerializer(ProductReview.objects.get(id=r_id)).data)
            except ProductReview.DoesNotExist:
                return Response({'ok': False, 'message': 'wrong review id', 'errors': 'review not found'})
            return Response(result)
        result.update(review=ProductReviewSerializer(ProductReview.objects.filter(product_id=p_id), many=True).data)
        return Response(result)
