# from django.db import models
# # django.core import validators as v
# from django.contrib.auth.models import AbstractUser
# from newsapp import NewsUser

# class Article(models.Model):
#     title = models.CharField(max_length=255)
#     url = models.URLField()
#     source = models.CharField(max_length=255)
#     published_date = models.DateTimeField()
#     content = models.TextField(null=True, blank=True)
    
#     author = models.CharField(max_length=255, null=True, blank=True)  # Optional author field
#     image_url = models.URLField(null=True, blank=True)  # Optional image URL
#     summary = models.TextField(null=True, blank=True)  # Optional summary for the article
#     category = models.CharField(max_length=255, null=True, blank=True)  # Optional category field

#     def __str__(self):
#         return self.title


# class SavedArticle(models.Model):
#     user = models.ForeignKey(NewsUser, on_delete=models.CASCADE)  # ForeignKey to NewsUser
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     saved_on = models.DateTimeField(auto_now_add=True)
    
#     is_favorite = models.BooleanField(default=False)  # Optional favorite flag
#     notes = models.TextField(null=True, blank=True)  # Optional user notes for saved article

#     def __str__(self):
#         return f'{self.user.email} saved {self.article.title}'
