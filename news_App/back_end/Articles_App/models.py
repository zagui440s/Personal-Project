from django.db import models
from newsapp.models import NewsUser

class Article(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    source = models.CharField(max_length=255)
    published_date = models.DateTimeField()
    content = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class SavedArticle(models.Model):
    user = models.ForeignKey(NewsUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="No title provided") 
    description = models.TextField(default="No description provided", blank=True, null=True)
    url = models.URLField(default="No URL provided")
    saved_on = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title