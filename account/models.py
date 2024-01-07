from django.contrib.auth.models import AbstractUser
from django.db.models import *
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = EmailField(unique=True, verbose_name=_('email'))
    password = CharField(max_length=256, verbose_name=_('password'))
    gender = BooleanField(default=True, verbose_name=_('gender'))
    REQUIRED_FIELDS = ['email', 'password']
    photo = ImageField(upload_to='profile_pics', null=True, blank=True, verbose_name=_('profile photo'))
    phone = CharField(max_length=13, unique=True, verbose_name=_('phone'))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'


class Employee(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    responsibility = CharField(max_length=32, verbose_name=_('responsibility'))
    salary = PositiveIntegerField(verbose_name=_('salary'))
    manager = ManyToManyField('self', verbose_name=_('manager'), related_name='employees')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
        db_table = 'employee'
