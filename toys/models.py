from django.db import models


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


class User(models.Model):
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True, blank=True)

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    def __str__(self):
        return self.first_name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Toy(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='toys', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tag, related_name='toys')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
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
    company = models.ForeignKey(Company, related_name='employee',  on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name


