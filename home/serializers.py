from rest_framework import serializers
from .models import SiteInfo, ClientsInfo, CompanyInfo, WorkingTime, Contact, Reviews, SiteReviews
from account.serializers import UserSerializer, EmployeeSerializer


class WorkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingTime
        fields = '__all__'
        read_only_fields = ['from_time', 'to_time', 'is_active']


class SiteInfoSerializer(serializers.ModelSerializer):
    work_time = WorkingTimeSerializer(read_only=True)

    class Meta:
        model = SiteInfo
        fields = '__all__'
        read_only_fields = ['site_title', 'site_icon', 'site_description', 'work_time', 'is_active']


class ClientsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsInfo
        fields = '__all__'
        read_only_fields = ['users', 'online', 'reviews', 'mid_rate', 'date']


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        read_only_fields = ['description', 'photo', 'is_active', 'html_page']


class ContactSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['employee', 'site']


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
        abstract = True


class SiteReviewsSerializer(ReviewsSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SiteReviews
        fields = '__all__'
