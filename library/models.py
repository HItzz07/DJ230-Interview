from django.db import models

# Create your models here.
class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100)
    no_of_copies = models.IntegerField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)

class Members(models.Model):
    member_id = models.IntegerField(primary_key=True)
    member_name = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)

class Circulation(models.Model):
    circulation_id = models.AutoField(primary_key=True) 
    book_id = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    member_id = models.ForeignKey(Members, on_delete=models.SET_NULL, null=True)
    checkout_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(Members, on_delete=models.SET_NULL, null=True)
    reservation_date = models.DateField(auto_now_add=True)
    fulfil = models.BooleanField(default=True)
    fulfilment_date = models.DateField(null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)
