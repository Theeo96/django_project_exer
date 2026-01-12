from rest_framework import serializers
from news.models.news import NewsItem

class NewsItemSerializer(serializers.ModelSerializer) :

    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta :
        model = NewsItem
        fields = ['id', 'title', 'link', 'description', 'source_title', 'created_at']

    def get_created_at(self, obj) :
        return obj.created_at.strftime('%Y년 %m월 %d일')