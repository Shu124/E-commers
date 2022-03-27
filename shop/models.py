from django.db import models


# Create your models here.
class product(models.Model):
    prod_id=models.AutoField
    prod_name=models.CharField( max_length=50)
    catagory=models.CharField( max_length=50 , default="")
    sub_catagory=models.CharField( max_length=50 , default="")
    price=models.IntegerField(default=0)
    desc=models.CharField( max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images' ,default="")
    
    
    def __str__(self):
        return self.prod_name



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class place_Order(models.Model):
    order_id=models.IntegerField(default=0)
    Items_json = models.CharField(max_length=5000)
    Name = models.CharField(max_length=90)
    Email = models.CharField(max_length=111)
    Address = models.CharField(max_length=111)
    City = models.CharField(max_length=111,)
    State = models.CharField(max_length=111)
    Zip_code = models.CharField(max_length=111)
    Phone = models.CharField(max_length=111)

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."