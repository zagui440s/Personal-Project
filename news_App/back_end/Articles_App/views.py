from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from django.conf import settings
from .models import Article, SavedArticle
from .serializers import ArticleSerializer, SavedArticleSerializer
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
        serializer = SavedArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

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
            return Response(articles[:3], status=HTTP_200_OK)  # Return only the first 3 articles
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)