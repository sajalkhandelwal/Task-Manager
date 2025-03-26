from django.db import models
from django.contrib.auth.models import User

class User(User, models.Model):  # Extends default Django User
    """
    Uses https://docs.djangoproject.com/en/3.2/topics/db/models/#proxy-models so that we can create a proxy model which
    doesn't create a table but actually populates all the fields required by engine.Query
    """

    class Meta:
        proxy = True

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    TASK_TYPE_CHOICES = [
        ('personal', 'Personal'),
        ('work', 'Work'),
        ('shopping', 'Shopping'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES, default='personal')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
