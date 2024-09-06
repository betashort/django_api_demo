from rest_framework import status, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import AooHold, AooRegister, Book
from .serializers import AooHoldSerializer, AooRegisterSerializer, BookSerializer

# Create your views here.
class BookListCreateAPIView(views.APIView):
    """本モデルの取得・登録APIのクラス"""
    
    #取得
    def get(self, request, *args, **kwargs):
        
        #モデルオブジェクトの一覧を取得する
        book_list = Book.objects.all()
        #シリアライザオブジェクトを作成する
        serializer = BookSerializer(instance = book_list, many=True)
        #レスポンスを返す
        return Response(serializer.data)
    
    #登録
    def post(self, request, *args, **kwargs):
        #シリアライザオブジェクトを作成する
        serializer = BookSerializer(data=request.data)
        #バリデーションチェック
        serializer.is_valid(raise_exception=True)
        #モデルオブジェクトを登録する
        serializer.save()
        #レスポンスを返す
        return Response(serializer.data, status.HTTP_201_CREATED)

class AooHoldAPIView(views.APIView):
    
    def get(self, request, *args, **kwargs):
        #一覧を取得する
        aoo_hold_list = AooHold.objects.all()
        #シリアライズする
        serializer = AooHoldSerializer(instance = aoo_hold_list, many=True)
        #レスポンスを返す
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        #シリアライズする
        serializer = AooHoldSerializer(data=request.data)
        #バリデーションチェックする
        serializer.is_valid(raise_exception=True)
        #データを登録する
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class AooRegisterAPI(views.APIView):
    
    def post(self, request, *args, **kwargs):
        #シリアライズする
        serializer = AooRegisterSerializer(data=request.data)
        #バリデーションチェックする
        serializer.is_valid(raise_exception=True)
        #データを登録する
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class AooRegisterMemberAPI(views.APIView):
    
    def get(self, request, pk, *args, **kwargs):
        #pkと一致する一覧を取得する
        aoo_register_members = AooRegister.objects.filter(aoo_id=pk, user_participation=True)
        #シリアライズする
        serializer = AooRegisterSerializer(instance=aoo_register_members, many=True)
        #レスポンスを返す
        return Response(serializer.data)
    