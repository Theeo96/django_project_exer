from django.http import JsonResponse
from rest_framework.views import APIView

from news.models import Sample

class HelloWorldView(APIView):
    def get(self, request):

        sample_queryset = Sample.objects.all()

        sample_list = list()

        for sample in sample_queryset :
            sample_list.append({
                "id": sample.id,
                "title": sample.title,
                "content": sample.content,
            })
        
        return JsonResponse(dict(
            status="OK",
            message="조회에 성공했습니다!",
            data=sample_list
        ))
    
    def post(self, request):

        title = request.data.get("title")
        content = request.data.get("content")

        sample = Sample.objects.create(title=title, content=content)

        return JsonResponse(dict(
            status="OK",
            message="'{}' 이 생성되었습니다.".format(sample.title),
            data=dict(
                id=sample.id,
                title=sample.title,
                content=sample.content
            )
        ))
    