from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class HomeView(APIView):

    @staticmethod
    def get_data(
            site: bool | None = True,
            work_time: bool | None = None,
            contacts: bool | None = None,
            reviews: bool | None = None,
            clients: bool | None = None,
            company: str | None = None
    ) -> dict:
        result = {}
        site_info = SiteInfo.objects.get(is_active=True)
        if site:
            result.update(site=SiteInfoSerializer(site_info).data)
        if work_time:
            result = WorkingTimeSerializer(site_info.working_times.get(is_active=True)).data
        if contacts:
            result.update(contacts=ContactSerializer(site_info.contacts.all(), many=True).data)
        if clients:
            result.update(clients=ClientsInfoSerializer(ClientsInfo.objects.all(), many=True).data)
        if company:
            result.update(company=CompanyInfoSerializer(CompanyInfo.objects.get(is_active=True)).data)
        if reviews:
            result.update(reviews=SiteReviewsSerializer(SiteReviews.objects.all(), many=True).data)
        return result

    def get(self, request):
        data = self.get_data(**request.query_params)
        return Response(data)
