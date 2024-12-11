from django.db import models
from django.contrib.auth.models import User


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