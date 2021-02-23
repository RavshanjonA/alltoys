from django.db import models


class ActiveObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class User(models.Model):
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField()

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    def __str__(self):
        return self.first_name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Toy(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='toys', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField(Tag, related_name='toys')
