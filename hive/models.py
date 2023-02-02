from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver
STATE_CHOICES=(
('Abia','Abia'),
('Adamawa','Adamawa'),
('Akwa Ibom','Akwa Ibom'),
('Anambra', 'Anambra'),
('Bauchi', 'Bauchi'),
('Bayelsa', 'Bayelsa'),
('Benue', 'Benue'),
('Borno', 'Borno'),
('Cross River', 'Cross River'),
('Delta', 'Delta'),

)
'''Ebonyi
Edo
Ekiti
Enugu
Gombe
Imo
Jigawa
Kaduna
Kano
Katsina
Kebbi
Kogi
Kwara
Lagos
Nasarawa
Niger
Ogun
Ondo
Osun
Oyo
Plateau
Rivers
Sokoto
Taraba
Yobe
Zamfara'''
	
class Customer(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	mobile = models.IntegerField(default=0)
	state = models.CharField(choices=STATE_CHOICES, max_length=100)
	def __str__(self):
	  return self.name
	
class Product(models.Model):
    CHOICES=(
    ('MN', 'Men'),
		('WM', 'Women'),
		('UN', 'Unisex'),
		('KD', 'Kids'),
    ('UW', 'Underwear'),
		('GW', 'Gowns'),
		('ST', 'Suits'),
    ('TR', 'Trousers'),
    ('SH', 'Shirts'),
    ('FW', 'Footwears'),
    ('PJ', 'Pyjamas'),
    ('SK', 'Skirts'),
    ('JN', 'Jeans'),
    ('SR', 'Shorts'),
    ('HD', 'Hoodies'),
    
)

    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.TextField()
 
    
    category = MultiSelectField(choices=CHOICES , max_length=15)
    
    def __str__(self):
        return self.name