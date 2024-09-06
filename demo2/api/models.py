import uuid
from django.db import models

# Create your models here.
class Book(models.Model):
    """本モデル"""
    #データベースのテーブル名
    class Meta:
        db_table = 'book'
    
    #book id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #book title
    title = models.CharField(verbose_name="タイトル", max_length=20, unique=True)
    #book price
    price = models.IntegerField(verbose_name="価格", null=True, blank=True)
    #created date
    created_at = models.DateTimeField(verbose_name="登録日", auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class AooHold(models.Model):
    """AOOの開催データ"""
    #データベースのテーブル名
    class Meta:
        db_table = "AOO_HOLD"
    
    #id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #aoo title
    title = models.CharField(verbose_name="AOO開催タイトル", max_length=20, unique=True)
    #created date
    created_at = models.DateTimeField(verbose_name="登録日", auto_now_add=True)

class AooRegister(models.Model):
    """AOOの出欠確認"""
    #データベースのテーブル名
    class Meta:
        db_table = "AOO_REGISTER"
    
    #id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #aoo title
    aoo_id = models.ForeignKey(AooHold, verbose_name="AOO開催タイトル", on_delete=models.PROTECT, null=True, blank=True)
    #aoo_title = models.CharField(verbose_name="AOO開催タイトル", max_length=20)
    #user name
    user_name = models.CharField(verbose_name="ユーザ名", max_length=20)
    #user participation
    user_participation = models.BooleanField(verbose_name="参加可否", null=True, blank=True)
    #created date
    created_at = models.DateTimeField(verbose_name="登録日", auto_now_add=True)