from django.contrib import admin
from .models import SiteInfo, ClientsInfo, CompanyInfo, Contact, SiteReviews, WorkingTime

admin.site.register(SiteInfo)
admin.site.register(ClientsInfo)
admin.site.register(CompanyInfo)
admin.site.register(Contact)
admin.site.register(SiteReviews)
admin.site.register(WorkingTime)
