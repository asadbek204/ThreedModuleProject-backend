from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class HomeView(APIView):

    def get_info(
            self,
            site: str | None = '1',
            contacts: str | None = '0',
            reviews: str | None = '0',
            clients: str | None = '0',
            company: str | None = '0',
            all_fields: str | None = '0',
            **kwargs
    ) -> dict:
        result = {}
        site_info = SiteInfo.objects.get(is_active=True)
        if self.check(site) or self.check(all_fields):
            result.update(site=SiteInfoSerializer(site_info).data)
        if self.check(contacts) or self.check(all_fields):
            result.update(contacts=ContactSerializer(site_info.contacts.all(), many=True).data)
        if self.check(clients) or self.check(all_fields):
            result.update(clients=ClientsInfoSerializer(ClientsInfo.objects.all(), many=True).data)
        if self.check(company) or self.check(all_fields):
            result.update(company=CompanyInfoSerializer(CompanyInfo.objects.get(is_active=True)).data)
        if self.check(reviews) or self.check(all_fields):
            result.update(reviews=SiteReviewsSerializer(SiteReviews.objects.all(), many=True).data)
        return result

    def get(self, request):
        return Response(self.get_info(**request.query_params))

    @staticmethod
    def check(obj) -> bool:
        return obj[0].lower() in ('true', 'yes', 'on', '1')
