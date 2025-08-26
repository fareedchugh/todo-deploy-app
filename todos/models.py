from django.db import models

class Todo(models.Model):
    # Add this line as the first field in your model
    id = models.BigAutoField(primary_key=True)
    
    # Your existing fields below (keep them as they are)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title