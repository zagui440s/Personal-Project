from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .models import Article, SavedArticle
from .serializers import ArticleSerializer, SavedArticleSerializer

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