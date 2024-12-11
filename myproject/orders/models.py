from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Order(models.Model):
    CATEGORY_CHOICES = [
        ('groceries', 'Groceries'),
        ('food', 'Food'),
        ('other', 'Other')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    location = models.CharField(max_length=255)
    items = models.TextField()
    preferred_delivery_time = models.TimeField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_claimed = models.BooleanField(default=False)
    delivery_agent = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='deliveries')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_reviews')
    reviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id} by {self.reviewer.username} for {self.reviewee.username}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    expected_delivery_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
