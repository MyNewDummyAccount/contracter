from django.db import models
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)


class Quote(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_requested = models.DateField()
    date_delivered = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()


class Task(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    details = models.TextField()


class Step(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(max_length=255)
    time_estimate = models.DecimalField(max_digits=5, decimal_places=2)
    material_description = models.TextField()
    material_estimate = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()


class Job(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.TextField()
    payed = models.BooleanField()


class Time(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date = models.DateField()
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    details = models.TextField()


class Material(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
