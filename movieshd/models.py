from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from datetime import timedelta
from datetime import datetime as dt
today= datetime.date.today()


class customer(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='static/images', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default='Male')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class publisher(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='static/images', null=True, blank=True)
    certificate = models.ImageField(upload_to='static/images', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default='Male')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name


class add_categories(models.Model):
    category_choice = [('Movie', 'Movie'), ('Show', 'Show'), ('Webseries', 'Webseries'), ('Kids', 'Kids')]
    language_choice = [('Telugu', 'Telugu'), ('Hindi', 'Hindi'), ('Tamil', 'Tamil'),
                       ('Malayalam', 'Malayalam'), ('Kannada', 'Kannada'), ('English', 'English')]
    geners_choice = [('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'),
                     ('Horror', 'Horror'), ('Thirller', 'Thirller'), ('Drama', 'Drama'),
                     ('Romance', 'Romance'), ('Sci Fi', 'Sci Fi')]
    uploader_name=models.CharField(max_length=500)
    category=models.CharField(max_length=500,choices=category_choice)
    title=models.CharField(max_length=500)
    discription = models.CharField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to="static/images", null=True, blank=True)
    language=models.CharField(max_length=500,choices=language_choice)
    geners=models.CharField(max_length=500,choices=geners_choice)
    screen_shot = models.ImageField(upload_to='static/images', null=True, blank=True)
    movie_length = models.CharField(max_length=50, null=True, blank=True)
    movie_director = models.CharField(max_length=200, null=True, blank=True)
    actor_name = models.CharField(max_length=1000, null=True, blank=True)
    movie_link = models.CharField(max_length=10000, null=True, blank=True)
    status=models.BooleanField(default=0)

    def __str__(self):
        return self.title



#### User Payment History
# class PayHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     order_id = models.CharField(max_length=200)
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.user.username

#### Membership
class Membership(models.Model):
    MEMBERSHIP_CHOICES = (
        ('Basic', 'Basic'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Premium', 'Premium'),
    )
    PERIOD_DURATION = (
        ('Days', 'Days'),
        ('Week', 'Week'),
        ('Months', 'Months'),
    )
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='Free', max_length=30)
    duration = models.PositiveIntegerField(default=7)
    duration_period = models.CharField(max_length=100, default='Day', choices=PERIOD_DURATION)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
       return self.membership_type

#### User Membership
class UserMembership(models.Model):
    user = models.OneToOneField(User, related_name='user_membership', on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, related_name='user_membership', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_id = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.user.username

@receiver(post_save, sender=UserMembership)
def create_subscription(sender, instance, *args, **kwargs):
    if instance:
        Subscription.objects.create(user_membership=instance,
                                    expires_in=dt.now().date() + timedelta(days=instance.membership.duration))

#### User Subscription
class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, related_name='subscription', on_delete=models.CASCADE, default=None)
    expires_in = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
      return self.user_membership.user.username

@receiver(post_save, sender=Subscription)
def update_acive(sender, instance, *args, **kwargs):
    if instance.expires_in < today:
        subscription=Subscription.objects.get(id=instance.id)
        subscription.delete()