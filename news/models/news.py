# info : dict_keys(['generator_detail', 'generator', 'title', 'title_detail', 'links', 'link', 'language', 'publisher', 'publisher_detail', 'rights', 'rights_detail', 'updated', 'updated_parsed', 'image', 'subtitle', 'subtitle_detail'])
# item: dict_keys(['title', 'title_detail', 'links', 'link', 'id', 'guidislink', 'published', 'published_parsed', 'summary', 'summary_detail', 'source'])

from news.models.common import BaseModel
from django.db import models

class NewsChannel(BaseModel) :
    generator = models.CharField(max_length=100, blank=True, null=True, verbose_name="제너레이터")
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name="제목")
    link = models.URLField(max_length=1000, blank=True, null=True, verbose_name="링크")
    language = models.CharField(max_length=10, blank=True, null=True, verbose_name="언어")
    publisher = models.CharField(max_length=100, blank=True, null=True, verbose_name="발행자")

    #updated update_at 에 넣으려고 함
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "뉴스 채널"


class NewsItem(BaseModel) :
    channel = models.ForeignKey(NewsChannel, on_delete=models.CASCADE, related_name="items", verbose_name="뉴스 채널")
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name="제목")
    link = models.URLField(max_length=1000, blank=True, null=True, verbose_name="링크")
    # "id"
    guid = models.CharField(max_length=5000, blank=True, null=True, verbose_name="GUID")
    # summary
    description = models.TextField(blank=True, null=True, verbose_name="설명")
    # soruce. href, title
    source_title = models.CharField(max_length=500, blank=True, null=True, verbose_name="신문사 이름")
    source_url = models.URLField(max_length=1000, blank=True, null=True, verbose_name="신문사 URL")


