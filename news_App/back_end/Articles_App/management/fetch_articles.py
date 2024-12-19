import requests
from django.core.management.base import BaseCommand
from Articles_App.models import Article

class Command(BaseCommand):
    help = 'Fetch articles from the News API and save them to the database'

    def handle(self, *args, **kwargs):
        apiKey = 'c62dfdb3cde04e6f8df156e446ae9b8a'
        country = 'us'  # You can change this to any country code
        url = f'https://newsapi.org/v2/top-headlines?country={country}&pageSize=3&apiKey={apiKey}'

        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            for article_data in articles:
                article, created = Article.objects.get_or_create(
                    title=article_data['title'],
                    defaults={
                        'url': article_data['url'],
                        'source': article_data['source']['name'],
                        'published_date': article_data['publishedAt'],
                        'content': article_data.get('content'),
                        'author': article_data.get('author'),
                        'image_url': article_data.get('urlToImage'),
                        'summary': article_data.get('description'),
                        'category': article_data.get('category', 'General'),
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added article: {article.title}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Article already exists: {article.title}'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch articles from the News API'))