from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)  # Name of the category
#     slug = models.SlugField(unique=True)  # Unique identifier for URL

#     def __str__(self):
#         return self.name
    
# class Properties(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='properties')
#     title = models.CharField(max_length=255)
#     property_type = models.CharField(max_length=100, choices=[
#         ('land', 'Land'),
#         ('house', 'House'),
#         ('hostel', 'Hostel'),
#         ('car', 'Car'),
#     ])
#     description = models.TextField()
#     location = models.CharField(max_length=255)
#     overview1 = models.CharField(max_length=100, blank=True, default="")
#     overview2 = models.CharField(max_length=100, blank=True, default="")
#     overview3 = models.CharField(max_length=100, blank=True, default="")
#     overview4 = models.CharField(max_length=100, blank=True, default="")
#     overview5 = models.CharField(max_length=100, blank=True, default="")
#     amenities1 = models.CharField(max_length=100, blank=True, default="")
#     amenities2 = models.CharField(max_length=100, blank=True, default="")
#     amenities3 = models.CharField(max_length=100, blank=True, default="")
#     amenities4 = models.CharField(max_length=100, blank=True, default="")
#     amenities5 = models.CharField(max_length=100, blank=True, default="")
#     amenities6 = models.CharField(max_length=100, blank=True, default="")
#     rental_price_per_month = models.DecimalField(max_digits=10, decimal_places=2)  # Monthly rent
#     number_of_rooms_available = models.PositiveIntegerField()  # Number of rooms available for rent
#     price = models.DecimalField(max_digits=10, decimal_places=2)  # For both sale price or rent price
#     number_of_bedrooms = models.IntegerField()
#     number_of_bathrooms = models.IntegerField()
#     lease_duration = models.CharField(max_length=50)  # e.g., '1 year', '6 months'
#     size_in_sqft = models.FloatField()
#     is_furnished = models.BooleanField(default=False)
#     is_available = models.BooleanField(default=True)  # Whether there are rooms available to rent
#     is_sold = models.BooleanField(default=False)  # Whether the land has been sold
#     date_posted = models.DateTimeField(auto_now_add=True)
#     contact_email = models.EmailField()
#     contact_phone = models.CharField(max_length=15)
#     image1 = models.ImageField(upload_to='images1/', blank=True, null=True)
#     image2 = models.ImageField(upload_to='images2/', blank=True, null=True)
#     image3 = models.ImageField(upload_to='images3/', blank=True, null=True)
    
    
#     def __str__(self):
#         return f"{self.title}"


class House(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=100, default="House")
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # For both sale price or rent price
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    size_in_sqft = models.FloatField()
    is_furnished = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    image1 = models.ImageField(upload_to='house_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='house_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='house_images/', blank=True, null=True)
    slug = models.SlugField(unique=True, default="")

    class Meta:
        abstract = True  # Base model, won't be created in the DB directly

# House for Rent model
class HouseForRent(House):
    rental_price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    lease_duration = models.CharField(max_length=50)  # e.g., '1 year', '6 months'
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} (For Rent)"

# House for Sale model
class HouseForSale(House):
    sale_price = models.DecimalField(max_digits=15, decimal_places=2)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (For Sale)"



# Abstract base class for common car fields
class Car(models.Model):
    
    make = models.CharField(max_length=255)  # e.g., Toyota, Honda
    model = models.CharField(max_length=255)  # e.g., Corolla, Civic
    year = models.PositiveIntegerField()  # e.g., 2020, 2021
    content = models.CharField(max_length=100, default="Car")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # For both rent or sale price
    mileage = models.PositiveIntegerField()  # Mileage in kilometers
    fuel_type = models.CharField(max_length=50)  # e.g., Petrol, Diesel, Electric
    transmission = models.CharField(max_length=50)  # e.g., Automatic, Manual
    location = models.CharField(max_length=255)  # e.g., city or specific address
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    date_posted = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to='car_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='car_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='car_images/', blank=True, null=True)
    slug = models.SlugField(unique=True, default="")
    

    class Meta:
        abstract = True  # Base model, won't be created directly in the DB

# Car for Rent model
class CarForRent(Car):
    rental_price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    rental_duration_options = models.CharField(max_length=100, blank=True, null=True)  # e.g., 'Daily, Weekly, Monthly'


    def __str__(self):
        return f"{self.make} {self.model} (For Rent)"

# Car for Sale model
class CarForSale(Car):
    sale_price = models.DecimalField(max_digits=15, decimal_places=2)
    is_sold = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.make} {self.model} (For Sale)"



class LandForSale(models.Model):
    title = models.CharField(max_length=255)  # Title for the land listing
    content = models.CharField(max_length=100, default="Land")
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)  # Address or general location of the land
    price = models.DecimalField(max_digits=15, decimal_places=2)  # Sale price of the land
    size_in_acres = models.DecimalField(max_digits=10, decimal_places=2)  # Size in acres or square feet
    is_sold = models.BooleanField(default=False)  # Whether the land has been sold
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    date_posted = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to='land_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='land_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='land_images/', blank=True, null=True)
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return f"{self.title} - {self.location} (For Sale)"



class HostelForRent(models.Model):
    title = models.CharField(max_length=255)  # Name or title of the hostel listing
    content = models.CharField(max_length=100, default="Hostel")
    description = models.TextField(blank=True, null=True)  # Details about the hostel
    location = models.CharField(max_length=255)  # City or neighborhood where the hostel is located
    rental_price_per_month = models.DecimalField(max_digits=10, decimal_places=2)  # Monthly rent
    number_of_rooms_available = models.PositiveIntegerField()  # Number of rooms available for rent
    room_type = models.CharField(max_length=100, choices=[  # Type of room
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('shared', 'Shared Room'),
    ])
    amenities = models.TextField(blank=True, null=True)  # E.g., Wi-Fi, electricity, water, etc.
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    is_available = models.BooleanField(default=True)  # Whether there are rooms available to rent
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    date_posted = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to='hostel_images/', blank=True, null=True)  # Optional image of the hostel
    image2 = models.ImageField(upload_to='hostel_images/', blank=True, null=True)  # Optional image of the hostel
    image3 = models.ImageField(upload_to='hostel_images/', blank=True, null=True)  # Optional image of the hostel
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return f"{self.title} - {self.location} (For Rent)"




class Contact(models.Model):
    name = models.CharField(max_length=255)  # Name of the person contacting
    email = models.EmailField()  # Email of the person
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Phone number (optional)
    message = models.TextField()  # Message sent by the person
    date_submitted = models.DateTimeField(auto_now_add=True)  # Automatically records the submission date

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Testimonial(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="testiminial_img")
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name_plural = "Testimonials"
        ordering = ['-date_added']
        
    def __str__(self):
        return f"{self.name} - {self.title} testimonial"