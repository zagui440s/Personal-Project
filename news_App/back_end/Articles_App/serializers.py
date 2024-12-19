from rest_framework import serializers
from .models import Article, SavedArticle

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class SavedArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedArticle
        fields = '__all__'
        read_only_fields = ['user']