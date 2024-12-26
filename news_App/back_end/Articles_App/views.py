from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from django.conf import settings
from .models import Article, SavedArticle, Comment
from .serializers import ArticleSerializer, SavedArticleSerializer, CommentSerializer
import requests

class ArticleListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

class SavedArticleListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        saved_articles = SavedArticle.objects.filter(user=request.user)
        serializer = SavedArticleSerializer(saved_articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = SavedArticleSerializer(data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class SavedArticleDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return SavedArticle.objects.get(pk=pk, user=user)
        except SavedArticle.DoesNotExist:
            return None

    def get(self, request, pk):
        saved_article = self.get_object(pk, request.user)
        if saved_article is None:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = SavedArticleSerializer(saved_article)
        return Response(serializer.data)

    def put(self, request, pk):
        saved_article = self.get_object(pk, request.user)
        if saved_article is None:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = SavedArticleSerializer(saved_article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        saved_article = self.get_object(pk, request.user)
        if saved_article is None:
            return Response(status=HTTP_404_NOT_FOUND)
        saved_article.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class FetchArticles(APIView):
    authentication_classes = []  # No authentication required
    permission_classes = []  # No permission required

    def get(self, request):
        api_key = settings.NEWS_API_KEY
        url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            articles = response.json().get('articles', [])
            return Response(articles[:10], status=HTTP_200_OK)  # Return only the first 3 articles
        except requests.exceptions.RequestException as e:
            return Response({"error": "Failed to fetch articles from News API."}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        

class CommentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, article_id):
        comments = Comment.objects.filter(article_id=article_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, article_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, article_id=article_id)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)