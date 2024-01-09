from rest_framework.response import Response
from rest_framework.views import APIView
from product.serializers import *


def detail(catalogs):
    return [
        {
            'catalog': CatalogSerializer(cat).data,
            'sub_catalogs': SubCatalogSerializer(sub_cat := SubCatalog.objects.filter(catalog=cat), many=True).data,
            'descriptions': {
                str(sub_cat.id): DescriptionSerializer(Description.objects.filter(category=sub_cat), many=True).data
            }
        } for cat in catalogs]


class CatalogView(APIView):
    @staticmethod
    def get(request, gender: str):
        gender = gender.lower() in ("1", "male", "man")
        catalogs = Catalog.objects.filter(gender=gender)
        return Response({'ok': True, 'catalogs': detail(catalogs)})


class CatalogsView(APIView):
    @staticmethod
    def get(request):
        catalogs = Catalog.objects.all()
        return Response({'ok': True, 'catalogs': detail(catalogs)})
