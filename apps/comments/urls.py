from django.urls import path

from apps.comments.views import create_comment

urlpatterns = [
    path('<int:category_id>/<int:article_id>/comment_success/',  create_comment, name='create_comment'),
    ]