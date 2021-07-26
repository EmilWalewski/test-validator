from django.urls import path
from .views import article_list, article_Detail, ArticleAPIView, ArticleDetails

urlpatterns = [
    #path('test/', article_list),
    path('test/', ArticleAPIView.as_view()),
    path('detail/<int:pk>/', ArticleDetails.as_view())
    #path('detail/<int:pk>/', article_Detail),
]
