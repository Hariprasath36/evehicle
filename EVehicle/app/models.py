from django.conf import settings
from django.db import models
from django.utils import timezone
STS = (
    ('','Select'),
    ('Approved','Approve'),
    ('Rejected','Reject'),
)
BTS = (
    ('','Select'),
    ('Available','Available'),
    ('Booked','Booked'),
)
class EVBunk_Detail(models.Model):
    bunk_name = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    company_address = models.CharField(max_length=200)
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    image = models.FileField('Upload Image',upload_to='documents/',null=True)
    def __str__(self):
    	return self.bunk_name
class Public_Detail(models.Model):
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.TextField(max_length=2000)
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    image = models.FileField('Upload Image',upload_to='documents/',null=True)
    def __str__(self):
        return self.username
class Slot_Detail(models.Model): 
    bunk_id = models.ForeignKey(EVBunk_Detail, on_delete=models.CASCADE,null=True)
    slot_name = models.CharField(max_length=30)
    status = models.CharField(max_length=30,choices=BTS,null=True)
    def __str__(self):
        return self.slot_name
class Booking(models.Model):
    bunk_id =  models.ForeignKey(EVBunk_Detail, on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(Public_Detail, on_delete=models.CASCADE,null=True)
    slot_id = models.ForeignKey(Slot_Detail, on_delete=models.CASCADE,null=True)
    type_of_battery = models.CharField(max_length=200,unique=True)
    battery_details = models.TextField(max_length=2000,null=True,blank=True)
    slot_status = models.CharField(max_length=30)
    status = models.CharField(max_length=30,choices=STS,null=True)
    date = models.DateField()
    time = models.CharField(max_length=200,unique=True)
    notes = models.TextField(max_length=2000,null=True,blank=True)
    amount = models.CharField(max_length=30,null=True,blank=True)
    payment_status = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.user_id.username
