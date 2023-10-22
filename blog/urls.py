from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, AboutView

app_name = 'article'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('about/', AboutView.as_view(), name='article-about'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]