from django.db import models

class SampleModel(models.Model):
    title = models.CharField(max_name=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Note: This is a basic model example. You should modify the model fields according to your web app's requirements.