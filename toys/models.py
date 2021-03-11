import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone

from toys.enum import ToyTypeEnum


class ActiveObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    street = models.CharField(max_length=100, help_text="name of street")
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return self.street

    class Meta:
        verbose_name_plural = 'Address'


class User(AbstractUser, BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.PROTECT, related_name='address', null=True, blank=True)

    class Meta:
        db_table = 'user'
        verbose_name_plural = 'Users'

    def __str__(self):
        if self.last_name:
            return f'{self.last_name} {self.first_name}'
        return self.first_name


class Tag(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


def logo_upload_path(instance, filename):
    current_dt = timezone.now()
    return f'toy_photos/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'


class Toy(BaseModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='toys', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=ToyTypeEnum.max_length(), choices=ToyTypeEnum.get_value_tuples(), null=True,
                            blank=True)
    photo = models.ImageField(upload_to=logo_upload_path, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tag, related_name='toys')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys:get_detail', args=(self.id,))

    class Meta:
        verbose_name_plural = 'Toys'


class Company(BaseModel):
    name = models.CharField(max_length=50)
    decription = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, related_name='employee', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name
