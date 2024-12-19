# from django.urls import path
# from .views import Sign_up, Log_in, Log_out, Info

# urlpatterns = [
    
# ]
from django.urls import path
from .views import ArticleListView, SavedArticleListView, FetchArticles

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('saved-articles/', SavedArticleListView.as_view(), name='saved-article-list'),
    path('fetch-articles/', FetchArticles.as_view(), name='fetch_articles')
]