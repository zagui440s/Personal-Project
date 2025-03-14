from django.urls import path
from .views import ArticleListView, SavedArticleListView, SavedArticleDetailView, FetchArticles

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('saved-articles/', SavedArticleListView.as_view(), name='saved-article-list'),
    path('saved-articles/<int:pk>/', SavedArticleDetailView.as_view(), name='saved-article-detail'),
    path('fetch-articles/', FetchArticles.as_view(), name='fetch_articles')
]