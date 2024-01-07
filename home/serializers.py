from rest_framework import serializers
from .models import SiteInfo, ClientsInfo, CompanyInfo, WorkingTime, Contact, Reviews, SiteReviews
from account.serializers import UserSerializer, EmployeeSerializer


class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInfo
        fields = '__all__'


class ClientsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsInfo
        fields = '__all__'
        read_only_fields = '__all__'


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        read_only_fields = '__all__'


class WorkingTimeSerializer(serializers.ModelSerializer):
    site = SiteInfoSerializer(read_only=True)

    class Meta:
        model = WorkingTime
        fields = '__all__'
        read_only_fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    site = SiteInfoSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Reviews
        fields = '__all__'
        abstract = True


class SiteReviewsSerializer(ReviewsSerializer):
    site = SiteInfoSerializer(read_only=True)

    class Meta:
        model = SiteReviews
        fields = '__all__'
