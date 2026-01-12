from django.http import JsonResponse
from rest_framework.views import APIView

from news.models.news import NewsItem
from news.serializers.news import NewsItemSerializer

class NewsListView(APIView):

    def get(self, request):

        news_item_queryset = NewsItem.objects.all()
        serializer = NewsItemSerializer(news_item_queryset, many=True)

        return JsonResponse(dict(
            status="OK",
            message="전체 리스트 조회에 성공했습니다!",
            data=serializer.data
        ))