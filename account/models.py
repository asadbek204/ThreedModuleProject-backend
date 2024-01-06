from django.contrib.auth.models import AbstractUser
from django.db.models import *


class User(AbstractUser):
    email = EmailField(unique=True, verbose_name='email')
    password = CharField(max_length=256, verbose_name='password')
    gender = BooleanField(default=True, verbose_name='gender')
    REQUIRED_FIELDS = ['email', 'username', 'password']
    photo = ImageField(upload_to='profile_pics', verbose_name='profile photo')
    phone = CharField(max_length=13, unique=True, verbose_name='phone')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'


class Employee(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    responsibility = CharField(max_length=32, verbose_name='responsibility')
    salary = PositiveIntegerField(verbose_name='salary')
    manager = ManyToManyField('self', verbose_name='manager', related_name='employees')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
        db_table = 'employee'
