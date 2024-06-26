from django.db.models import *
from account.models import Employee, User
from django.utils.translation import gettext_lazy as _


class WorkingTime(Model):
    from_time = TimeField()
    to_time = TimeField()
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.from_time.strftime('') + ' - ' + self.to_time.strftime('')

    class Meta:
        verbose_name = 'working time'
        verbose_name_plural = 'working times'
        db_table = 'working_time'


class SiteInfo(Model):
    site_title = CharField(
        max_length=128,
        default=_('Terra Pro: Clothing store in Tashkent ≡ Men\'s and women\'s clothing on Terrapro.uz'), blank=True)
    site_icon = ImageField(upload_to='info/site/')
    site_description = TextField(
        default=_(
            'Terra Pro - Manufacturer of men\'s and women\'s clothing at competitive prices ⭐️ Clothing store in'
            'Uzbekistan ✔️ Trying on and fast delivery of clothes ☎ +998 71 2509391 | Clothing store Terrapro.uz'
        ),
        blank=True
    )
    work_time = OneToOneField(WorkingTime, on_delete=CASCADE, related_name='site_info', verbose_name=_('work time'))
    phone = CharField(max_length=13, default='+998712509391')
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = 'site info'
        verbose_name_plural = 'site info'
        db_table = 'site_info'


class ClientsInfo(Model):
    users = PositiveIntegerField(default=0, verbose_name=_('quantity of users'))
    online = PositiveIntegerField(default=0, verbose_name=_('online user'))
    reviews = PositiveIntegerField(default=0, verbose_name=_('quantity of review'))
    mid_rate = PositiveSmallIntegerField(default=0, verbose_name=_('average rate'))
    date = DateField(auto_now=False, auto_now_add=False, verbose_name=_('month'))

    def __str__(self):
        return f"{self.users}"

    class Meta:
        verbose_name = 'clients info'
        verbose_name_plural = 'clients info'
        db_table = 'clients_info'


class CompanyInfo(Model):
    description = TextField()
    photo = ImageField(upload_to='company/photos/', blank=True, null=True, verbose_name=_('company logo'))
    html_page = FileField(upload_to='company/pages/', blank=True, null=True, verbose_name=_('company page'))
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.description[:10]

    class Meta:
        verbose_name = 'company info'
        verbose_name_plural = 'company info'
        db_table = 'company_info'


class Contact(Model):
    employee = ForeignKey(Employee, on_delete=CASCADE, related_name='employees_contacts', verbose_name=_('employee'))
    site = ForeignKey(SiteInfo, on_delete=CASCADE, related_name='contacts')

    def __str__(self):
        return self.employee.user.username

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        db_table = 'contact'


class Reviews(Model):
    stars = IntegerField(default=0)
    comment = TextField()
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:10]

    class Meta:
        abstract = True


class SiteReviews(Reviews):
    user = ForeignKey(User, on_delete=CASCADE, related_name='site_reviews', verbose_name=_('user'))
    site = ForeignKey(SiteInfo, on_delete=CASCADE)

    class Meta:
        verbose_name = 'Site Review'
        verbose_name_plural = 'Site Reviews'
        db_table = 'site_review'
