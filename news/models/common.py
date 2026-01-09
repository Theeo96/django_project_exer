from django.db import models
import uuid

class ModelManager(models.Manager) :

    def get_queryset(self):
        return super().get_queryset().filter(removed_at=None)

class BaseModel(models.Model):

    objects = ModelManager()

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, verbose_name="ID")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    removed_at = models.DateTimeField(blank=True, null=True, verbose_name="삭제일")
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name="수정일")

    class Meta:
        abstract = True

