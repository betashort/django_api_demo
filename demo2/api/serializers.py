from rest_framework import serializers
from .models import AooHold, AooRegister, Book

class BookSerializer(serializers.ModelSerializer):
    """本モデル用のシリアライザー"""
    class Meta:
        #対象のモデルクラスを指定する
        model = Book
        #利用するモデルのフィールドを指定する
        fields = ['title', 'price']

class AooHoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = AooHold
        fields = ["id", "title"]

class AooRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AooRegister
        fields = ["aoo_id", "user_name", "user_participation"]
        