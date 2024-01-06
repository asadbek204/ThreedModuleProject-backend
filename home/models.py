from django.db.models import *
from account.models import Employee, User


class SiteInfo(Model):
    site_title = CharField(
        max_length=128,
        default='Terra Pro: Clothing store in Tashkent ≡ Men\'s and women\'s clothing on Terrapro.uz')
    site_icon = ImageField(upload_to='')
    site_description = TextField(
        default='Terra Pro - Manufacturer of men\'s and women\'s clothing at competitive prices ⭐️ Clothing store in '
                'Uzbekistan ✔️ Trying on and fast delivery of clothes ☎ +998 71 2509391 | Clothing store Terrapro.uz'
    )

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = 'site info'
        verbose_name_plural = 'site info'
        db_table = 'site_info'


class ClientsInfo(Model):
    users = PositiveIntegerField(default=0)
    online = PositiveIntegerField(default=0)
    reviews = PositiveIntegerField(default=0)
    mid_rate = PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.users

    class Meta:
        verbose_name = 'clients info'
        verbose_name_plural = 'clients info'
        db_table = 'clients_info'


class CompanyInfo(Model):
    description = TextField()
    photo = ImageField(upload_to='company/photos/', blank=True, null=True)
    html_page = FileField(upload_to='company/pages/', blank=True, null=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.description[:10]

    class Meta:
        verbose_name = 'company info'
        verbose_name_plural = 'company info'
        db_table = 'company_info'


class WorkingTime(Model):
    site = ForeignKey(SiteInfo, on_delete=CASCADE)
    from_time = TimeField()
    to_time = TimeField()
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.from_time.strftime('') + ' - ' + self.to_time.strftime('')

    class Meta:
        verbose_name = 'working time'
        verbose_name_plural = 'working times'
        db_table = 'working_time'


class Contact(Model):
    employee = ForeignKey(Employee, on_delete=CASCADE)
    site_info = ForeignKey(SiteInfo, on_delete=CASCADE)

    def __str__(self):
        return self.employee.user.phone

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        db_table = 'contact'


class Reviews(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='reviews')
    stars = IntegerField(default=0)
    comment = TextField()
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True


class SiteReviews(Reviews):

    class Meta:
        verbose_name = 'Site Review'
        verbose_name_plural = 'Site Reviews'
        db_table = 'site_review'
