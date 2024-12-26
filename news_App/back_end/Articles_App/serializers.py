from rest_framework import serializers
from .models import Article, SavedArticle, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class SavedArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedArticle
        fields = ['id', 'user', 'title', 'description', 'url', 'saved_on', 'is_favorite', 'notes']
        read_only_fields = ['user', 'saved_on']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Comment
        fields = ['id', 'article', 'user', 'content', 'created_at']
        read_only_fields = ['user', 'created_at']