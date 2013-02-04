from django.shortcuts import render_to_response
from website.models import Article

def index(request):
    articles = Article.objects.order_by('-date')
    return render_to_response('website/home.html', { 'articles': articles } )

def article(request, article_id):
    article = Article.objects.filter(id=int(article_id))[0]
    return render_to_response('website/article.html', { 'article': article } )