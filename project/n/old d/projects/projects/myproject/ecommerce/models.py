from django.db import models
from django.urls import reverse
from django.utils import  timezone
from datetime import datetime
from django.conf import settings
from django.template.defaultfilters import slugify
from django.db.models import Sum
import random
# Create your models here.



generate_random_num_for_order_id = (random.randint(45995, 67995))




class Products(models.Model):

    cartigories = [

            ('POPULAR CATEGORIES',(
              ('Fashion','Fashion'),
              ('Electronics','Electronics'),
              ('Computer','Computer'),
              ('Beauty','Beauty'),
              ('Sport','Sport'),

            )

         ),

        ('TRENDING PRODUCTS', (
            ('Top_10', 'Top 10'),
            ('Womens', 'Womens'),
            ('Mens', 'Mens'),
            ('Kids', 'Kids'),
            ('Accessories', 'Accessories'),

        )

         ),

        ('NEW ARRIVAL', (
            ('Televisons', 'Televisons'),
            ('Computer', 'Computer'),
            ('Jewelry', 'Jewelry'),
            ('Apparel', 'Apparel'),
            ('Apparel', 'Apparel'),



            )

         )

]

    class Colors(models.TextChoices):

        Yellow= 'YL'
        Red= 'RD'
        Orange = 'OR'
        Green= 'GR'



    product_name= models.CharField(max_length=200, null=True, blank=True)
    product_image= models.ImageField(null=True, blank=True, upload_to='assets/product')
    product_description= models.TextField(max_length=200, null=True, blank=True)
    price= models.FloatField(default=0, null=True)
    Cartegory = models.CharField(max_length=30, choices=cartigories, default='Top_10')
    color= models.CharField(max_length=200, choices=Colors.choices, default=Colors.Red)
    slug= models.SlugField(null=True, blank=True, help_text='Please put a url name')




    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Products, self).save(*args, **kwargs)

    def __str__(self):

        return self.product_name

    def get_absolute_url(self):
        return reverse('product', kwargs={
            'slug': self.slug})

    def imageURL(self):

        try:
            url = self.product_image.url
        except:
            url = ''

        return url


    def get_add_to_cart(self):
        return reverse('addtocart', kwargs={
            'slug':self.slug
        })

    def get_clear_cart(self):
        return reverse('clearcart', kwargs={
            'slug':self.slug
        })

    def sum_rating(self):

        rating= self.rating_set.all()

        total= sum([item.rated for  item in rating])

        product= ([p.product.product_name for  p in rating])

        divide_sum = int(total) / 3

        index_divide_sum = str(divide_sum)[:3]
        # print(index_divide_sum)

        if float(index_divide_sum) > 5:
            total=5.0
            return total

        if (len(product) != len(set(product))):

            return index_divide_sum
        return total


    def get_sub_images(self):

        sub_images= self.subimages_set.all()

        return sub_images

    def get_user_reviews(self):

        user_reviews = self.productreviews_set.all()[:5]
        # print(user_reviews)
        return user_reviews

    def get_count_reviews(self):

        count_review= self.get_user_reviews().count()
        # print(count_review)
        return count_review

    def get_total_order_product(self):

        total= self.order_set.all()
        return total.count()

    # class Meta:
    #     ordering = ['rating__product', 'price']

class Orderitem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user',null=True, blank=True)
    item = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)
    device_name= models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):

        return str(self.item)

    def get_increase_qty(self):
        return reverse('increase', kwargs={
            'slug': self.item.slug
        })

    def get_decrease_qty(self):
        return reverse('decrease', kwargs={
            'slug': self.item.slug
        })

    def get_price(self):
        orderitem = self.quantity * self.item.price

        return orderitem

    def get_delete_an_item(self):
        return reverse('delete_an_item', kwargs={
            'slug':self.item.slug
        })





class Order(models.Model):
    myuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users',null=True, blank=True)
    orderitem= models.ForeignKey(Products, on_delete=models.CASCADE, default=0)
    user_quantity= models.IntegerField(default=0)
    ordered = models.BooleanField(default=False)
    total= models.FloatField(default=0, blank=True, null=False)
    reference_id= models.CharField(max_length=50, null=True, blank=True)
    order_id= models.CharField(max_length=200, blank=True, null=True)
    start_date= models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField(default=timezone.now)
    completed= models.BooleanField(default=False)

    def __str__(self):

        return str(self.myuser)



class ShippingAddress(models.Model):

    State_origin =[
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwayibom', 'Akwayibom'),
        ('Akwayibom', 'Akwayibom'),

    ]

    City = [
        ('Abia', '   Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwayibom', 'Akwayibom'),
        ('Akwayibom', 'Akwayibom'),

    ]

    myuser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_address', null=True,
                               blank=True,)
    full_name= models.CharField(max_length=200, null=True, blank=True)
    mobile_phone_number= models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    state_of_origin= models.CharField(max_length=30, choices=State_origin, default='Abia')


    def __str__(self):

        return  str(self.myuser)

    def get_absolute_url(self):

        return reverse('account')


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rate', null=True, blank=True)
    product= models.ForeignKey(Products, on_delete=models.CASCADE)
    rated= models.DecimalField(decimal_places=1, max_digits=5)

    def __str__(self):
        return self.product.product_name


class SubImages(models.Model):
    product= models.ForeignKey(Products, on_delete=models.CASCADE)
    img1= models.ImageField(null=True, blank=True, upload_to='assets/product')
    img2= models.ImageField(null=True, blank=True, upload_to='assets/product')
    img3= models.ImageField(null=True, blank=True, upload_to='assets/product')
    img4= models.ImageField(null=True, blank=True, upload_to='assets/product')


    def __str__(self):
        return self.product.product_name

    def imageURL1(self):

        try:
            url = self.img1.url
        except:
            url = ''

        return url

    def imageURL2(self):

        try:
            url = self.img2.url
        except:
            url = ''

        return url


    def imageURL3(self):

        try:
            url = self.img3.url
        except:
            url = ''

        return url


    def imageURL4(self):

        try:
            url = self.img4.url
        except:
            url = ''

        return url




class ProductReviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                             blank=True)
    product= models.ForeignKey(Products, null=True, on_delete=models.CASCADE)
    date_added= models.DateTimeField(default=timezone.now)
    your_review = models.TextField(null=True, blank=True)
    rating= models.DecimalField(max_digits=5, decimal_places=1, default=0.0,)

    def __str__(self):
        return self.user.username

    class Meta:

        ordering = ['-date_added']

