from rest_framework import serializers
from apps.blog.models import Article, BlogCategory, Tag
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields= ('id', 'name')
class BlogCategorySerializer(serializers.Serializer):
    class Meta:
        model = BlogCategory
        fields = ('id', 'name','image')
class ArticleWriteSerializer(serializers.ModelSerializer):
    tag = serializers.ListField(child=serializers.CharField(max_length=64), write_only=True)
    class Meta:
        model = Article
        fields = (
            "id",
            "category",
            "image",
            "title",
            "text_preview",
            "text",
            "publish_date",
            "tag"
        )
class ArticleReadSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer()
    tag = TagSerializer(many=True)
    class Meta:
        model = Article
        fields = (
            "id",
            "category",
            "image",
            "title",
            "text_preview",
            "text",
            "publish_date",
            "user",
            "created_at",
            # "image_thumbnail",
            "tag"
        )