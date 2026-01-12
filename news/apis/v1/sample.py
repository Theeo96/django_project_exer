from django.http import JsonResponse
from rest_framework.views import APIView

from news.models import Sample

from news.models.news import NewsItem
from news.serializers.news import NewsItemSerializer

class SampleListView(APIView):

    def get(self, request):

        # news_item_queryset = NewsItem.objects.all()[:10]
        # serializer = NewsItemSerializer(news_item_queryset, many=True)

        # response_json = serializer.data

        sample_queryset = Sample.objects.all()

        sample_list = list()

        for sample in sample_queryset :
            sample_list.append(dict(
                id=sample.id,
                title=sample.title,
                content=sample.content
            ))
        
        return JsonResponse(dict(
            status="OK",
            message="전체 리스트 조회에 성공했습니다!",
            data=sample_list
        ))
    
    def post(self, request):

        sample = Sample.objects.create(
            title=request.data.get("title"),
            content=request.data.get("content")
        )

        return JsonResponse(dict(
            status="OK",
            message="생성에 성공했습니다!".format(sample.title),
            data=dict(
                id=sample.id,
                title=sample.title,
                content=sample.content
            )
        ))

class SampleDetailView(APIView) :
    def get(self, request, sample_id):

        sample = Sample.objects.get(id=sample_id)
        
        return JsonResponse(dict(
            status="OK",
            message="{} 조회에 성공했습니다!".format(sample_id),
            data=dict(
                id=sample.id,
                title=sample.title,
                content=sample.content
            )
        ))
    
    def put(self, request, sample_id):

        sample = Sample.objects.get(id=sample_id)
        title=request.data.get("title", None),
        content=request.data.get("content", None)

        is_modified = False
        
        if title is not None :
            is_modified = True
            sample.title = title
        
        if content is not None :
            is_modified = True
            sample.content = content
        
        if is_modified :
            sample.save()

        return JsonResponse(dict(
            status="OK",
            message="수정에 성공했습니다!"
        ))

    def delete(self, request, sample_id) :
        
        Sample.objects.filter(id=sample_id).delete()

        return JsonResponse(dict(
            status="OK",
            message="{} 삭제에 성공했습니다!".format(sample_id)
        ))